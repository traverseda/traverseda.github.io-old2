#!/usr/bin/env python3
from streams import pagesFromFiles, savePageChanges, index, render, markd
from collections import defaultdict

def main():
    pages = pagesFromFiles("./content")
    pages = sorted(pages,key=lambda x:x['created'],reverse=True) #Sort pages by when they were created
#    pages = markd(pages) #Render the text. I should figure out a way to do this lazily.
    pages = list(pages)
    indexes = defaultdict(list)
    for page in pages:
        for tag in page['tags']:
            indexes[tag].append(page)
    for key, values in indexes.items():
        index(values,key,"index.html")
        index(values,key,"rss.xml",outpath="index/{name}_{page}.rss")
    for page in pages:
        render(page,"blogPost.html")
        savePageChanges(page)
    tagsList = {
        'indexes':indexes,
        'tags':{k:len(v) for k,v in indexes.items()},
        'name':'List of tags',
    }
    render(tagsList,"tagsList.html",outpath='index/tagsList.html')

if __name__ == "__main__":
    main()
