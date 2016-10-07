# rndrr

this is a small python utility to render a jinja2 template based on variables defined in a [TOML](https://github.com/toml-lang/toml) configuration file

## usage

	python3 rndrr.py -c tests/case1.toml -f tests/case1.j2 

or

	cat tests/case1.j2 | python3 rndrr.py -c tests/case1.toml
