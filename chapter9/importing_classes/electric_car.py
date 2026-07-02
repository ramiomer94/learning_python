"""A set of classes that can be used to represent electric cars."""
from car import Car
class Battery() : 
    """ A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=70) :
        """ Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self) :
        """ Print a statement describing the battery size. """
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    
    def upgrade_battery(self) :
        """ Set the battery size to 85. """
        if self.battery_size != 85 :
            self.battery_size = 85
    
    def get_range(self) : 
        """ print a statement about the range this battery provides."""
        if self.battery_size == 70 :
            range = 240
        elif self.battery_size == 85 :
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
    


class ElectricCar(Car) :
    """ Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year) :
        """ Initialize attributes of the parent class. 
            Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
    
    def fill_gas_tank(self) :
        """ Electric cars don't have gas tanks. """
        print("This car doesn't need a gas tank!")
