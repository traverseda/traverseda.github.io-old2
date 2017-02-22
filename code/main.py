#!/bin/env python3
import random, parse, ruamel.yaml, arrow, hashlib
from os import listdir
from os.path import isfile, join, basename
from settings import *
from collections import ChainMap, defaultdict


yml_string="```yaml\n{}\n```"

def splitData(text):
    """This function strips yaml out of the first segment, and returns it as data.
    """
    splitText = text.split("\n---\n")
    data = dict()
    if len(splitText) > 1:
        data = parse.parse(yml_string, splitText[0])[0]
        data = ruamel.yaml.load(data, ruamel.yaml.RoundTripLoader)
        text="\n---\n".join(splitText[1:])
    return (data, text)

def joinData(data, text):
    yml = ruamel.yaml.dump(data, Dumper=ruamel.yaml.RoundTripDumper)
    yml = yml_string.format(yml)
    newText="\n---\n".join((yml,text))
    return newText

template = env.get_template('blogPost.html')
indexes=defaultdict(list)
def renderBlog(filePath):
    f = open(filePath, 'r').read()
    baseName = basename(filePath)+".html"
    data, content = splitData(f)
    data = ChainMap(data, defaultOptions)
    if data['published']:
        print("Compiling "+filePath)
        context = {}
        context['blogContent'] = content
        context['blogData'] = data
        context['name']=baseName

        renderOut = template.render(**context)
        o = open('../'+baseName,'w+').write(renderOut)
        data['lastRender']=str(arrow.utcnow())
        if "createdDate" not in data:
            data.createdDate=str(arrow.utcnow())

        pageObject={
            'data':data,
            'content':content,
            'name':baseName,
            'file':filePath,
        }
        if 'tags' in data:
            for i in data['tags']:
                indexes[i].append(pageObject)
    else:
        print("Ignoring "+filePath)
    newText = joinData({key:value for key, value in data.items()}, content)
    f = open(filePath, 'w').write(newText)
    return baseName

pages=[]
for file in listdir("../rawPages/"):
    if file.endswith(".md"):
        pages.append('../rawPages/'+file)

[i for i in map(renderBlog, pages)]
