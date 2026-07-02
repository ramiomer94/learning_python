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


    
resturant = Resturant('subway', 'fast food')
print("The name of the resturant is " + resturant.resturant_name.title() + ".")
print("The cuisine type of the resturant is " + resturant.cuisine_type + ".")
print("The number of customers served is " + 
    str(resturant.number_served) + ".")

resturant.number_served = 10
print("The number of customers served is " + 
    str(resturant.number_served) + ".")

resturant.set_number_served(20)
resturant.print_number_served()

resturant.increment_number_served(5)
resturant.print_number_served()