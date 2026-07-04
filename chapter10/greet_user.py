from pathlib import Path
import json

path = Path('username.json')

try :
    username = json.loads(path.read_text())
except FileNotFoundError :
    print(f"The file {path} does not exist")
else :
    print(f"Wlecome back, {username.title()}")