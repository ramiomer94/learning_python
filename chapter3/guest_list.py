guest_names = ['mo', 'ronaldo', 'zlatan'];
print("Dear " + guest_names[0].title() + ", you are cordially invited to dinner on Christmas Eve.");
print("Dear " + guest_names[1].title() + ", you are cordially invited to dinner on Christmas Eve.");
print("Dear " + guest_names[2].title() + ", you are cordially invited to dinner on Christmas Eve.");


print("Unfortunately, " + guest_names[1].title() + " has declined the invitation!");
guest_names[1] = 'zidan';

print("\nUpdated Invitation List:");
print("The number of guest we are inviting is: " + str(len(guest_names)) + ".");
print("Dear " + guest_names[0].title() + ", you are cordially invited to dinner on Christmas Eve.");
print("Dear " + guest_names[1].title() + ", you are cordially invited to dinner on Christmas Eve.");
print("Dear " + guest_names[2].title() + ", you are cordially invited to dinner on Christmas Eve.");

print("\n\nWe have found a bigger dinner table and we have decided to extend the invitation to more people!!");

guest_names.insert(0, "omar");
guest_names.insert(2, "steph");
guest_names.append("wemby");
print("The number of guest we are inviting is: " + str(len(guest_names)) + ".");
print("Dear " + guest_names[0].title() + ", you are cordially invited to dinner on Christmas Eve.");
print("Dear " + guest_names[1].title() + ", you are cordially invited to dinner on Christmas Eve.");
print("Dear " + guest_names[2].title() + ", you are cordially invited to dinner on Christmas Eve.");
print("Dear " + guest_names[3].title() + ", you are cordially invited to dinner on Christmas Eve.");

print("\nI am sorry but we just received the news that the bigger table won't be available in time so we might have to shrink the invitation list.");
print("Sorry " + guest_names.pop().title() + "! We have to rescind the dinner invitation.");
print("Sorry " + guest_names.pop().title() + "!  We have to rescind the dinner invitation.");
print("Sorry " + guest_names.pop().title() + "! We have to rescind the dinner invitation.");
print("Sorry " + guest_names.pop().title() + "! We have to rescind the dinner invitation.");
print("The number of guest we are inviting is: " + str(len(guest_names)) + ".");


print("\n");
print("Dear " + guest_names[0].title() + ", you are cordially invited to dinner on Christmas Eve.");
print("Dear " + guest_names[1].title() + ", you are cordially invited to dinner on Christmas Eve.");

del guest_names[0];
del guest_names[0];
print("The number of guest we are inviting is: " + str(len(guest_names)) + ".");
print(guest_names);

