from pathlib import Path

path = Path('guest.txt')
guest_name = input("Enter your full name: ")
path.write_text(guest_name.title())
