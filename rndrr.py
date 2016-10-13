import sys
import argparse
import pytoml as toml

from jinja2 import Template

def parseArgs():
    parser = argparse.ArgumentParser(description="rndrr.py")
    parser.add_argument("-c", "-conf", dest="confFilename", required=True, help="template configuration")
    parser.add_argument("-f", "-file", dest="tmplFilename", required=False, help="template")
    parser.add_argument("-o", "-out", dest="outFilename", required=False, help="output")
    return parser.parse_args()

def askValues(d, askCode, printStr, copy=True):
    if copy:
        do = d.copy()
    else:
        do = d
    for k,v in do.items():
        if isinstance(v, dict):
            askValues(v, askCode, printStr % (str(k) + ".%s"), False)
        elif v == askCode:
            do[k] = input(printStr % str(k)) 
        else:
            pass

    return do


ctxt = parseArgs()

# read template config
with open(ctxt.confFilename, "r") as f:
    confStr = f.read()

conf = toml.loads(confStr)
if ctxt.tmplFilename is not None:
    conf = askValues(conf, "<interactive>", "enter value for %s: ")

# read template
if ctxt.tmplFilename is None:
    tmplStr = sys.stdin.read()
else:
    with open(ctxt.tmplFilename, "r") as f:
        tmplStr = f.read()

tmpl = Template(tmplStr)

# render and print
if ctxt.outFilename is None:
    print(tmpl.render(**conf))
else:
    with open(ctxt.outFilename, "w") as f:
        f.write(tmpl.render(**conf))
