#!/bin/env python3
import random, parse, ruamel.yaml, arrow, hashlib
from os import listdir
from os.path import isfile, join, basename
from settings import *
from collections import ChainMap, defaultdict

from utils import splitData, joinData

template = env.get_template('blogPost.html')
indexes=defaultdict(list)
def renderBlog(filePath, changed=False):
    f = open(filePath, 'r').read()
    baseName = basename(filePath)+".html"
    data, content = splitData(f)
    data = ChainMap(data, defaultOptions)
    checksum = hashlib.sha256(content.encode('utf-8')).hexdigest()
    if data['contentHash'] == None:
        newText = joinData({key:value for key, value in data.items()}, content)
        f = open(filePath, 'w').write(newText)

    if  checksum != data['contentHash']:
        changed = True
        data['contentHash'] = checksum

    if data["published"]:
        if 'firstPublish' not in data:
            data['firstPublish'] = str(arrow.utcnow())

        pageObject={
            'data':data,
            'content':content.split("\n---\n"),
            'name':baseName,
            'file':filePath,
        }

        if 'tags' in data:
            for i in data['tags']:
                indexes[i].append(pageObject)
    if data["published"] and changed:
        print("Compiling "+filePath)
        context = {}
        context['data']=data
        context['blogContent'] = content
        context['blogData'] = data
        context['name']=baseName

        renderOut = template.render(**context)
        o = open('../'+baseName,'w+').write(renderOut)
        data['lastRender']=str(arrow.utcnow())
        if "createdDate" not in data:
            data.createdDate=str(arrow.utcnow())
        newText = joinData({key:value for key, value in data.items()}, content)
        f = open(filePath, 'w').write(newText)
    else:
        print("Ignoring "+filePath)


pages=[]
for file in listdir("../rawPages/"):
    if file.endswith(".md"):
        pages.append('../rawPages/'+file)


indexTemplate = env.get_template('index.html')
rssTemplate = env.get_template('rss.xml')
def renderIndex(item):
    key, pages = item
    print("Generating index: "+key)
    orderedPages = sorted(pages, key=lambda page: arrow.get(page['data']['firstPublish'])) 
    context = {
        'pages':orderedPages,
        'name':key,
    }
    renderOut = indexTemplate.render(**context)
    o = open('../index/'+key+'.html','w+').write(renderOut)
    renderOut = rssTemplate.render(**context)
    o = open('../index/'+key+'.xml','w+').write(renderOut)


import argparse

parser = argparse.ArgumentParser(description='Build a static site')
parser.add_argument('--build-all', dest='build_all', action='store_const',
                   const=True, default=False,
                   help='rebuild all pages, ignoring checksums')
parser.add_argument('--build-search', dest='build_search', action='store_const',
                   const=True, default=False,
                   help='Rebuild the lunr.js search index')

if __name__ == "__main__":
    args = parser.parse_args()
    if args.build_all:
        [i for i in map(lambda page: renderBlog(page, changed=True), pages)]
    else:
        [i for i in map(renderBlog, pages)]
    foo = [i for i in map(renderIndex, indexes.items())]

    if args.build_search:
        pass
