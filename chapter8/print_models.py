from printing_functions import print_models, show_completed_models

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print(unprinted_designs)

print()
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# The slice notation [:] makes a copy of the list to send to the function.
# If we didn’t want to empty the list of unprinted designs in print_models.py,
# we could call print_models() like this:

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)