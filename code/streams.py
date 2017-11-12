import arrow

defaultOptions={
    'published':False,
    'tags': ['home',],
    'created':str(arrow.utcnow()),
    'updated':str(arrow.utcnow()),
}

from pathlib import Path
from collections import ChainMap, defaultdict
from utils import splitData, joinData
from settings import jinjaEnv, OUTPUT_DIR, DEFAULT_CONTEXT

def pagesFromFiles(path, glob="**/*.md"):
    path=Path(path)
    files = path.glob(glob)
    for f in files:
        data, text = splitData(f.read_text())
        if not data:
            joinData(defaultOptions,text)
        if data and data['published']:
            out = ChainMap(data,defaultOptions)
            out['content']={ #Content is things that don't get added back into the yaml.
                'file':f,
                'text':text,
                'path':f.relative_to(path),
                'depth': len(f.relative_to(path).parents)-1
            }
            yield out

def savePageChanges(context):
    f=context['content']['file']
    text=context['content']['text']
    del context['content']
    f.write_text(joinData(context,text))

import mistune
from mistune_contrib.toc import TocMixin
from mdAddons import HighlightRendererMixin
class MdRenderer(HighlightRendererMixin,mistune.Renderer,TocMixin):
    pass
    
toc = MdRenderer()
mdRenderer = mistune.Markdown(escape=False,renderer=toc)
def markd(context):
    for page in context:
        toc.reset_toc()
        page['content']['html']= mdRenderer(page['content']['text'])
#        page['content']['toc']=copy(toc)
        yield page

def render(context,template,outpath=None):
    template = jinjaEnv.get_template(template)
    if not outpath:
        outpath=str(context['content']['path'])+".html"
    renderOut = template.render(**ChainMap(context,DEFAULT_CONTEXT))
    outFile = Path(OUTPUT_DIR+outpath)
    outFile.parent.mkdir(parents=True,exist_ok=True)
    outFile.write_text(renderOut)
    print("rendered",outpath)

def index(pages,name,template,outpath="index/{name}_{page}.html",count=20):
    indexGroup=[]
    indexGroups=[indexGroup,]
    for idx,page in enumerate(pages): #Group pages in groups of no more than $count
        if not idx+1/count:
            indexGroup=[]
            indexGroups.append(indexGroup)
        indexGroup.append(page)
    total = len(indexGroups)
    for idx, indexGroup in enumerate(indexGroups):
        context={
            'posts':indexGroup,
            'pageNum':idx,
            'pageCount':total,
            'name':name,
        }
        render(context,template,outpath.format(name=name,page=idx))

