players = ['charles', 'martina', 'michael', 'florence', 'eli'];
print(players[0:3]);
print(players[1:4]);

"""
If you omit the first index in a slice, Python automatically starts your
slice at the beginning of the list:

"""
print(players[:4]);

"""
A similar syntax works if you want a slice that includes the end of a list.
For example, if you want all items from the third item through the last item,
you can start with index 2 and omit the second index:

"""
print(players[2:]);

"""
Recall that a negative index returns an element a certain distance from the
end of a list; therefore, you can output any slice from the end of a list.
For example, if we want to output the last three players on the roster,
we can use the slice players[-3:]:

"""
print(players[-3:])

print("Here are the first three players on my team:");
for player in players[:3]:
    print(player);