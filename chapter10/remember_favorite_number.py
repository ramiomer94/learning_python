from pathlib import Path
import json

path = Path('number.json')

if path.exists() :
    number = json.loads(path.read_text())
    print(f"I know your favorite number! It's {number}.")
else :
    print(f"I can't figure out what your favorite number is.")