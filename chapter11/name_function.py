# def get_formatted_name(first, last) :
#    """Generate a neatly formatted full name"""
#    full_name = f"{first} {last}"
#    return full_name.title()

# What does a failing test look like? Let’s modify get_formatted_name()
#  so it can handle middle names, but let’s do so in a way that breaks
#  the function for names with just a first and last name, like Janis Joplin.

# def get_formatted_name(first, middle, last) :
#     """Generate a neatly formatted full name."""
#     full_name = f"{first} {middle} {last}"
#     return full_name.title()

# So when a test fails, don’t change the test. If you do, your tests
# might pass, but any code that calls your function like the test 
# does will suddenly stop working. Instead, fix the code that’s causing
# the test to fail. Examine the changes you just made to the function,
# and figure out how those changes broke the desired behavior.
# In this case, get_formatted_name() used to require only two parameters: 
# a first name and a last name. Now it requires a first name, middle name,
# and last name. The addition of that mandatory middle name parameter broke
# the original behavior of get_formatted_name(). The best option here is to
# make the middle name optional.

def get_formatted_name(first, last, middle='') :
    """Generate a neatly formatted full name."""
    if middle :
        full_name = f"{first} {middle} {last}"
    else :
        full_name = f"{first} {last}"
    
    return full_name.title()