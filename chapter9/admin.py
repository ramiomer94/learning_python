class User() :
    """ A class to represent a user's profile. """

    def __init__(self, first_name, last_name, age, location) :
        """ Initialize the user's profile. """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attemnpts = 0

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
    
    def increment_login_attempts(self) :
        """ Increment the value of login attempts by 1. """
        self.login_attemnpts += 1
    
    def reset_login_attempts(self) :
        """ Reset the value of the login attempts to 0. """
        self.login_attemnpts = 0

class Admin(User) :
    """ A class to represent an admin user. """

    def __init__(self,first_name, last_name, age, location ) :
        """ Initialize the admin user. 
            Then initialize the privileges attribute. 
        """
        super().__init__(first_name, last_name, age, location)
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    
    def show_privileges(self) :
        """ Display the privileges of the admin user. """
        print("\nThe admin user has the following privileges: ")
        for privilege in self.privileges :
            print("-" + privilege)

admin_user = Admin('jordan', 'poole', 25, 'detroit')
admin_user.describe_user()
admin_user.greet_user()
admin_user.show_privileges()