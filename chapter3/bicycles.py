bicycles = ['trek', 'cannondale', 'redline', 'specialized'];
print(bicycles);
print(bicycles[0]);
print(bicycles[0].title());
print(bicycles[1]);
print(bicycles[3]);

# Python has a special syntax for accessing the last element in a list. By asking for the item at index -1, Python always returns the last item in the list:
print(bicycles[-1]);

"""
This convention extends to other negative index
values as well. The index -2 returns the second item from the end of the list,
the index -3 returns the third item from the end, and so forth

"""


message = "My first bicycles was a " + bicycles[0].title() + ".";
print(message); 