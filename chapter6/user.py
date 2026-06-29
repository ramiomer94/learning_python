user_0 = {
    'username' : 'efermi',
    'first' : 'enrico',
    'last' : 'fermi', 
    };

"""
to write a for loop for a dictionary, you create names for
the two variables that will hold the key and value in each key-value pair. You
can choose any names you want for these two variables. 

The second half of the for statement at u includes the name of the dictionary
followed by the method items(), which returns a list of key-value pairs.
The for loop then stores each of these pairs in the two variables provided.
"""
for key, value in user_0.items() :
    print("\nKey : " + key);
    print("Value : " + value);