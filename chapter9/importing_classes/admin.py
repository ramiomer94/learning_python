""" A set of classes that can be used to represent an admin user"""

from user import User

class Privileges() :
    """ A class to represesnt the privileges of an admin user. """

    def __init__(
            self, privileges=['can add post', 'can delete post',
                              'can ban user',]
    ) :
        """ Initialize the privileges attribute. """
        self.privileges = privileges

    def show_privileges(self) :
        """ Display the privileges of the admin user. """
        print("\nThe admin user has the following privileges: ")
        for privilege in self.privileges :
            print("-" + privilege)

class Admin(User) :
    """ A class to represent an admin user. """

    def __init__(self,first_name, last_name, age, location ) :
        """ Initialize the admin user. 
            Then initialize the privileges attribute. 
        """
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()