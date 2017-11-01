import parse, ruamel.yaml, arrow, hashlib
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
            data = ruamel.yaml.load(parseResult[0], ruamel.yaml.RoundTripLoader)
            text="\n---\n".join(splitText[1:])
    return (data, text)

def joinData(data, text):
    yml = ruamel.yaml.dump(data, Dumper=ruamel.yaml.RoundTripDumper)
    yml = yml_string.format(yml)
    newText="\n---\n".join((yml,text))
    return newText

