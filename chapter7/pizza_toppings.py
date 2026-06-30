prompt = "\nPlease Enter the toppings you would like on your pizza: "
prompt += "\n(Enter 'quit' when you are finished.) "

active = True
while active :
    topping = input(prompt)
    if topping == 'quit' :
        active = False
    else :
        print("\nI will add " + topping + "to your pizza.");