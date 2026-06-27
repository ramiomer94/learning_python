age = 23;
message = "Happy " + str(age) + "rd Birthday";
print(message);

"""
age = 23
message = "Happy " + age + "rd Birthday!"
print(message)
You might expect this code to print the simple birthday greeting, Happy
23rd birthday! But if you run this code, you’ll see that it generates an error:
Traceback (most recent call last):
File "birthday.py", line 2, in <module>
message = "Happy " + age + "rd Birthday!"
u TypeError: Can't convert 'int' object to str implicitly

This is a type error. It means Python can’t recognize the kind of information you’re using.
In this example Python sees at u that you’re using a variable that has an integer value (int),
but it’s not sure how to interpret that value. Python knows that the variable could represent 
either the numerical value 23 or the characters 2 and 3. When you use integers within strings
like this, you need to specify explicitly that you want Python to use the integer as a string
of characters.You can do this by wrapping the variable in the str() function, which tells
Python to represent non-string values as strings.

"""