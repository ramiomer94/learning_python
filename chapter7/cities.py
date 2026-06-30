prompt = "\nPlease enter the name of cities you have vistited "
prompt += "\n(Enter 'quit' when you are finished.) ";

while True :
    city = input(prompt)
    if city == 'quit' :
        break
    else :
        print("I'd love to go to " + city.title() + "!")

