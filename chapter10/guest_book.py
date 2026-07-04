from pathlib import Path

filename = 'guest_book.txt'
path = Path(filename)


guest_names = ''
while True :
    guest_name = input("Enter your full name (or enter 'q' to quit): ")
    if guest_name == 'q' :
        break
    guest_names += f"{guest_name}\n"

path.write_text(guest_names)