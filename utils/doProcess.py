import json
import os
import subprocess


def doProcess(output=False):
    path = f"../daily-matches-scrapping/main.py"
    os.chdir(os.path.dirname(path))

    if output:
        process = subprocess.run(
            ['python', 'main.py', "save"], text=True, capture_output=True)

        return json.loads(process.stdout)

    subprocess.run(['python', 'main.py', "save"],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
