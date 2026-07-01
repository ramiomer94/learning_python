# Start with some designs that need to be printed
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs :
    current_design = unprinted_designs.pop();
    # Simulate creating a 3D print from the design.
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed: ")
for completed_model in completed_models :
    print(completed_model)

# We can reorganize this code by writing two functions, each of which
# does one specific job. Most of the code won’t change; we’re just making it
# more efficient. The first function will handle printing the designs, and the
# second will summarize the prints that have been made:

def print_models(unprinted_designs, completed_models) :
    """ 
    Simulate printing each design unil none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models) :
    """ Show all the models that were printred. """
    print("\nThe following models have been printed:")
    for completed_model in completed_models :
        print(completed_model)

print()
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