# I am going to import the show_magician() function from the
# magician_function module and call the function using each of these
# approaches:
#       import module_name
#       from module_name import function_name
#       from module_name import function_name as fn
#       import module_name as mn
#       from module_name import *

# import magicians_functions 

# magicians = ['messi', 'maradona', 'zidan', 'ronaldinho']
# magicians_functions.show_magicians(magicians)

# from magicians_functions import show_magicians
# magicians = ['messi', 'maradona', 'zidan', 'ronaldinho']
# show_magicians(magicians)

# from magicians_functions import show_magicians as sm
# magicians = ['messi', 'maradona', 'zidan', 'ronaldinho']
# sm(magicians)

# import magicians_functions as mf
# magicians = ['messi', 'maradona', 'zidan', 'ronaldinho']
# mf.show_magicians(magicians)

from magicians_functions import *
magicians = ['messi', 'maradona', 'zidan', 'ronaldinho']
show_magicians(magicians)