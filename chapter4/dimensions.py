dimensions = (200, 50);
print(dimensions[0]);
print(dimensions[1]);

"""
Let’s see what happens if we try to change one of the items in the tuple
dimensions:
The code at u tries to change the value of the first dimension, but
Python returns a type error. Basically, because we’re trying to alter a tuple,
which can’t be done to that type of object, Python tells us we can’t assign a
new value to an item in a tuple

"""

for dimension in dimensions:
    print(dimension);

print();
dimensions = (200, 50);
print("\noriginal dimensions: ");
for dimension in dimensions :
    print(dimension)

"""
Although you can’t modify a tuple, you can assign a new value to a variable
that holds a tuple. So if we wanted to change our dimensions, we could
redefine the entire tuple:

"""

dimensions = (400, 100);
print("\nModified dimensions:")
for dimension in dimensions :
    print(dimension);