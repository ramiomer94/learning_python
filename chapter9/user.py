class User() :
    """ A class to represent a user's profile. """

    def __init__(self, first_name, last_name, age, location) :
        """ Initialize the user's profile. """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self) :
        """ Describe the user's profile. """
        print("\nThe user's name is " + self.first_name.title() +
            " " + self.last_name.title() + ".")
        print("The user's age is " + str(self.age) + ".")
        print("The user lives in " + self.location.title() + ".")
    
    def greet_user(self) :
        """ Greet the user. """
        print("Hello, " + self.first_name.title() + " " +
            self.last_name.title() + "!")

user_0 = User('stephen', 'curry', 38, 'san francisco')
user_0.describe_user()
user_0.greet_user()

user_1 = User('kevin', 'durant', 37, 'Houston')
user_1.describe_user()
user_1.greet_user()

user_2 = User('luka', 'dončić', 25, 'los angeles')
user_2.describe_user()
user_2.greet_user()