from jinja2 import Template, Environment, FileSystemLoader
from webassets import Environment as AssetsEnvironment
from webassets.ext.jinja2 import AssetsExtension
assets_env = AssetsEnvironment('./assets', '/assets')
env = Environment(loader=FileSystemLoader('./templates'),extensions=[AssetsExtension])
env.assets_environment = assets_env

import random
def pickColour(text):
    #Picks a random colour based on a string.
    random.seed(text)
    c = random.choice(colors)
    return c
env.filters['pickColour']=pickColour

import mistune
from mdAddons import HighlightRendererMixin
class renderer(HighlightRendererMixin,mistune.Renderer):
    pass
markdown = mistune.Markdown(escape=False,renderer=renderer())

def markd(text):
    return markdown(text)
env.filters['markd']=markd

colors=['yellow','orange','red','magenta','violet','blue','cyan','green']
reserverdNames=['notes','code','index']

defaultOptions={
    'published':False,
    'stripHtml':False,
}
