import parse, arrow, hashlib
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

yml_string="```yaml\n{}\n```"
yml_extractor = parse.compile(yml_string)

def splitData(text):
    """This function strips yaml out of the first segment, and returns it as data.
    """
    splitText = text.split("\n---\n")
    data = dict()
    if len(splitText) > 1:
        parseResult = yml_extractor.parse(splitText[0])
        if parseResult:
            data = load(parseResult[0], Loader=Loader)
            text="\n---\n".join(splitText[1:])
    return (data, text)

def joinData(data, text):
    yml = dump(dict(data), Dumper=Dumper)
    yml = yml_string.format(yml)
    newText="\n---\n".join((yml,text))
    return newText

from jinja2 import Environment, FileSystemLoader
from webassets import Environment as AssetsEnvironment
from webassets.ext.jinja2 import AssetsExtension
assets_env = AssetsEnvironment('./assets', '/assets')
jinjaEnv = Environment(loader=FileSystemLoader('./templates'),extensions=[AssetsExtension])
jinjaEnv.assets_environment = assets_env

import mistune
from mistune_contrib.toc import TocMixin
from mdAddons import HighlightRendererMixin
class Renderer(HighlightRendererMixin,mistune.Renderer):
    pass

renderer = Renderer()
markdown = mistune.Markdown(escape=False,renderer=renderer)

def markd(text):
    return markdown(text)

import html
def obfuscate(text):
    obfuscated=['&#%d;' % ord(x) for x in text]
    obfuscated="".join(obfuscated)
    return obfuscated

def jinjify(text):
    t = jinjaEnv.from_string(text)
    return t.render()
