my_foods = ['pizza', 'falafel', 'carrot cake'];
friends_foods = my_foods[:];

print("My favorite foods are:");
print(my_foods);

print("\nMy friends' favorite foods:");
print(friends_foods);

"""
To prove that we actually have two separate lists, we’ll add a new food
to each list and show that each list keeps track of the appropriate person’s
favorite foods:

"""

my_foods.append('cannoli');
friends_foods.append('ice cream');

print("My favorite foods are:");
print(my_foods);

print("\nMy friends' favorite foods:");
print(friends_foods);

"""
If we had simply set friend_foods
equal to my_foods, we would not produce two separate lists. For example,
here’s what happens when you try to copy a list without using a slice:
Instead of storing a copy of my_foods in friend_foods at u, we set
friend_foods equal to my_foods. This syntax actually tells Python to connect
 the new variable friend_foods to the list that is already contained in
my_foods, so now both variables point to the same list. As a result, when we
add 'cannoli' to my_foods, it will also appear in friend_foods. Likewise 'ice
cream' will appear in both lists, even though it appears to be added only to
friend_foods.

"""
my_foods = ['pizza', 'falafel', 'carrot cake'];
friends_foods = my_foods;

print("My favorite foods are:");
for food in my_foods:
    print(food);

print("\nMy friends' favorite foods:");
for food in friends_foods:
    print(food);


my_foods.append('cannoli');
friends_foods.append('ice cream');

print("\nMy favorite foods are:");
for food in my_foods:
    print(food);

print("\nMy friends' favorite foods:");
for food in friends_foods:
    print(food);
