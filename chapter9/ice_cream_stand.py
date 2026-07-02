class Resturant() :
    """ A class to model a resturant. """
    
    def __init__(self, resturant_name, cuisine_type) :
        """ Initialize resturant attributes. """
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_resturant(self) :
        """ Describe the resturant: give the name and cuisine type. """
        print("\nThe resturant's name is " + self.resturant_name.title() + ".")
        print("The resturant's cuisine type is " + self.cuisine_type + ".")
    
    def open_resturant(self) :
        """ Indicates that the resturant is open. """
        print("We are open for business!")
    
    def set_number_served(self, number_customers) :
        """ Set the number of customers served. """
        if number_customers >= self.number_served :
            self.number_served = number_customers
        else :
            print("You can't roll back the number of customers served!")
    
    def increment_number_served(self, additional_customers) :
        """ Increment the number of customers served."""
        if additional_customers >= 0 :
            self.number_served += additional_customers
        else :
            print("You can't roll back the number of customers served!")
    
    def print_number_served(self) :
        """ print the number of customers served."""
        print("The number of customers served is " + 
            str(self.number_served) + ".")

class IceCreamStand(Resturant) :
    """ An attempt to model an ice cream stand as a specific kinf of resturant,
    """
    def __init__(self,resturant_name, cuisine_type='ice cream') :
        """ Initialize attributes of the parent class.
        Then initialize attributes specific to an ice cream stand."
        """
        super().__init__(resturant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry',
                        'cookies and cream']
    
    def print_flavors(self) :
        """ print a list of available ice cream flavors. """
        print("The available ice cream flavors are: ")
        for flavor in self.flavors :
            print("-" + flavor.title())
    
my_stand = IceCreamStand('dairy queen')
my_stand.describe_resturant()
my_stand.print_number_served()
my_stand.set_number_served(10)
my_stand.print_number_served()
my_stand.increment_number_served(5)
my_stand.print_number_served()
my_stand.print_flavors()