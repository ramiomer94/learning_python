def get_formatted_name(first_name, last_name) :
    """ Return a full name, neatly formatted """
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

def get_formatted_name(first_name, middle_name, last_name) :
    """ Return a full name, neatly formatted """
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

# This function works when given a first, middle, and last name. The
# function takes in all three parts of a name and then builds a string out of
# them. The function adds spaces where appropriate and converts the full
# name to title case:
#           John Lee Hooker
# But middle names aren’t always needed, and this function as written
# would not work if you tried to call it with only a first name and 
# a last name. To make the middle name optional, we can give the middle_name
#  argument an empty default value and ignore the argument unless the user
#  provides a value. To make get_formatted_name() work without a middle name,
#  we set the default value of middle_name to an empty string and move it to
#  the end of the list of parameters:

def get_formatted_name(first_name, last_name, middle_name = '') :
    if middle_name :
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else :
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

   
