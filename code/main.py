#!/bin/env python3
import shelve, random
from jinja2 import Template, Environment, FileSystemLoader
from os import listdir
from os.path import isfile, join, basename

from webassets import Environment as AssetsEnvironment
from webassets.ext.jinja2 import AssetsExtension
assets_env = AssetsEnvironment('./assets', '/assets')
env = Environment(loader=FileSystemLoader('./templates'),extensions=[AssetsExtension])
env.assets_environment = assets_env

colors=['yellow','orange','red','magenta','violet','blue','cyan','green']

def pickColour(text):
    #Picks a random colour based on a string.
    random.seed(text)
    c = random.choice(colors)
    return c
env.filters['pickColour']=pickColour

import mistune
markdown = mistune.Markdown(escape=False)
def markd(text):
    return markdown(text)

env.filters['markd']=markd

template = env.get_template('blogPost.html')

def renderBlog(filePath):
    f = open(filePath, 'r').read()
    baseName = basename(filePath)+".html"

    context = {}
    context['blogContent'] = f
    context['name']=baseName

    renderOut = template.render(**context)
    o = open('../'+baseName,'w+').write(renderOut)
    return baseName

#All notes are rendered. These ones are the only ones that
#Are going to end up getting listed though.
posts=[

]

notes=[]
for file in listdir("../notes/"):
    if file.endswith(".md"):
        notes.append('../notes/'+file)

print([i for i in map(renderBlog, notes)])
