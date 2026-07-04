from pathlib import Path
import json

number = int(input("What is your favorite number? "))

path = Path('number.json')
path.write_text(json.dumps(number))

