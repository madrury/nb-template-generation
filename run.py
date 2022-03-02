import json

template = open('template.ipynb', 'r').read()
config = json.load(open('config.json', 'r'))

for c in config:
    notebook = (
        template
            .replace("[OFFSET]", str(c["OFFSET"]))
            .replace("[EXPONENT]", str(c["EXPONENT"]))
    )
    with open(f"notebooks/plot:{c['OFFSET']}:{c['EXPONENT']}.ipynb", 'w') as f:
        f.write(notebook)