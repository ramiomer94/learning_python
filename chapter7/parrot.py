message = input("Tell me something and I will repeat it back to you: ");
print(message);

prompt = "\nTell me something and I will repeat it back to you: ";
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit' :
    message = input(prompt);
    if message != 'quit' :
        print(message);

"""
For a program that should run only as long as many conditions are true,
you can define one variable that determines whether or not the entire program
is active. This variable, called a flag, acts as a signal to the program. We
can write our programs so they run while the flag is set to True and stop
running when any of several events sets the value of the flag to False.
As a result, our overall while statement needs to check only one condition:
whether or not the flag is currently True. Then, all our other tests
(to see if an event has occurred that should set the flag to False) can be
neatly organized in the rest of the program.

"""

active = True
while active :
    message = input(prompt);
    if message == 'quit' :
        active = False
    else :
        print(message)