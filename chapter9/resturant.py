class Resturant() :
    """ A claas to model a resturant. """

    def __init__(self, resturant_name, cuisine_type) :
        """ Initialize resturant name and cuisine type attributes. """
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type
    
    def describe_resturant(self) :
        """ Describe the resturant: give the name and cuisine type. """
        print("\nThe resturant's name is " + self.resturant_name.title() + ".")
        print("The resturant's cuisine type is " + self.cuisine_type + ".")
    
    def open_resturant(self) :
        """ Indicates that the resturant is open. """
        print("We are open for business!")
    

local_resturant = Resturant('subway', 'fast food')
print("The name of the resturant is " + local_resturant.resturant_name.title() + ".")
print("The cuisine type of the resturant is " + local_resturant.cuisine_type + ".")

resturant_0 = Resturant('meet noodles', 'chinese')
resturant_0.describe_resturant()

resturant_1 = Resturant('pizza hut', 'italian')
resturant_1.describe_resturant()

resturant_2 = Resturant("osmow's", 'middle eastern')
resturant_2.describe_resturant()







