prompt = "Enter a number, and I'll tell you if it's a multiple of ten or not: "
number = int(input(prompt));

if number % 10 == 0 :
    print("The number " + str(number) + " is a multiple of ten.");
else :
    print("The number " + str(number) + " is not a multiple of ten.");