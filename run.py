import json
import subprocess

template = open('template.ipynb', 'r').read()
config = json.load(open('config.json', 'r'))

for c in config:
    notebook = (
        template
            .replace("[OFFSET]", str(c["OFFSET"]))
            .replace("[EXPONENT]", str(c["EXPONENT"]))
    )
    filenm = f"notebooks/plot:{c['OFFSET']}:{c['EXPONENT']}.ipynb"
    with open(f"notebooks/plot:{c['OFFSET']}:{c['EXPONENT']}.ipynb", 'w') as f:
        f.write(notebook)
    _ = subprocess.run(
        # jupyter nbconvert --to notebook --inplace --execute filled-in-template.ipynb
        ["jupyter", "nbconvert", "--to", "notebook", "--inplace", "--execute", filenm],
        stdout=subprocess.PIPE
    )