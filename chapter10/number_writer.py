from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
path = Path(filename)

contents = json.dumps(numbers)
path.write_text(contents)
