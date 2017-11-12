from utils import jinjaEnv, jinjify, markd, obfuscate
jinjaEnv.filters['jinja']=jinjify
jinjaEnv.filters['markd']=markd
jinjaEnv.filters['obfuscate']=obfuscate

OUTPUT_DIR="../"

DEFAULT_CONTEXT={
    "siteName":"With dread but cautious optimism",
    "content":{},
}
