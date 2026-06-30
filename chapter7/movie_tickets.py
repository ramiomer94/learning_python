
prompt = "\nHow old are you? "
prompt += "\n(Enter 0 to exit the program.) "

while True :
    age = input("How old are you? ");
    if age == 'quit' :
        break
    age = int(age)
    if age < 3 :
        print("Your ticket costs $0.")
    elif age < 12 :
        print("Your ticket costs $10.")
    else :
        print("Your ticket costs $15.")

print();
print();

# Use a conditional test in the while statement to stop the loop
age = -1
while age != 0 :
    age = int(input(prompt))
    if age == 0 :
        continue
    if age < 0:
        print("Invalid  age value. Age can't be negative.");
        continue

    if age < 3 :
        print("Your ticket costs $0.")
    elif age < 12 :
        print("Your ticket costs $10.")
    else :
        print("Your ticket costs $15.")
 
   
print();
print();

# Use an active variable to control how long the loop runs
active = True
while active :
    age = int(input(prompt))
    if age == 0 :
        active = False
        continue

    if age < 0:
        print("Invalid  age value. Age can't be negative.");
        continue

    if age < 3 :
        print("Your ticket costs $0.")
    elif age < 12 :
        print("Your ticket costs $10.")
    else :
        print("Your ticket costs $15.")


print();
print();

# Use a break statement to exit the loop when the user enters a 'quit' value
while True :
    age = input(prompt)
    if age == 'quit' :
        break
    age = int(age)
    if age <= 0:
        print("Invalid  age value. Age can't be negative.");
        continue

    if age < 3 :
        print("Your ticket costs $0.")
    elif age < 12 :
        print("Your ticket costs $10.")
    else :
        print("Your ticket costs $15.")