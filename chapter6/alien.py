alien_0 = {'color': 'green', 'points' : 5};
print(alien_0['color']);
print(alien_0['points']);

"""
The simplest dictionary has exactly one key-value pair, as shown in this
modified version of the alien_0 dictionary:

"""
alien_0 = {'color' : 'green'};

"""
To get the value associated with a key, give the name of the dictionary and
then place the key inside a set of square brackets, as shown here:

"""
print(alien_0['color']);
alien_0 = {'color' : 'green', 'points' : 5 };
new_points = alien_0['points'];
print("You just earned " + str(alien_0['points']) + " points.");

"""
To add a new key-value pair, you
would give the name of the dictionary followed by the new key in square
brackets along with the new value.

"""
print(alien_0);
alien_0['x_position'] = 0;
alien_0['y_position'] = 25;
print(alien_0)

alien_0 = {};

alien_0['color'] = 'green';
alien_0['points'] = 5;

print(alien_0);

alien_0 = {'color' : 'green'};
print("The alien is " + alien_0['color'] + ".");

alien_0['color'] = 'yellow';
print("The alien is " + alien_0['color'] + ".");

alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'};
print("Original x_position is: " + str(alien_0['x_position']));

if(alien_0['speed'] == 'slow') :
    x_increment = 1;
elif (alien_0['speed'] == 'medium') :
    x_increment = 2;
else:
    x_increment = 3;

alien_0['x_position'] = alien_0['x_position'] + x_increment;
print("New x_position: " + str(alien_0['x_position']));

alien_0 = {'color' : 'green', 'points' : 5};
print(alien_0);

del alien_0['points'];
print(alien_0);


