import sys
import argparse
import pytoml as toml

from jinja2 import Template

def parseArgs():
    parser = argparse.ArgumentParser(description="rndrr.py")
    parser.add_argument("-c", "-conf", dest="confFilename", required=True, help="template configuration")
    parser.add_argument("-f", "-file", dest="tmplFilename", required=False, help="template")
    return parser.parse_args()


ctxt = parseArgs()

# read template config
with open(ctxt.confFilename, "r") as f:
    confStr = f.read()

conf = toml.loads(confStr)

# read template
if ctxt.tmplFilename is None:
    tmplStr = sys.stdin.read()
else:
    with open(ctxt.tmplFilename, "r") as f:
        tmplStr = f.read()

tmpl = Template(tmplStr)

# render and print
print(tmpl.render(**conf))
