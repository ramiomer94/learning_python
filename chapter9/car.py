class Car() :
    """ A simple attempt to represent a car. """

    def __init__(self, make , model , year) :
        """ Initialize attributes to describe a car. """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self) :
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self) :
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    # It can be helpful to have methods that update certain attributes for you.
    # Instead of accessing the attribute directly, you pass the new value to a
    # method that handles the updating internally.
    # Here’s an example showing a method called update_odometer():
    def update_odometer(self, mileage) :
        """ Set the odometer reading to the given value. 
        Reject the change if it attempts to roll the odometer back. 
        """
        if mileage >= self.odometer_reading :
            self.odometer_reading = mileage
        else : 
            print("You can't roll back an odometer!")

    
    # Sometimes you’ll want to increment an attribute’s value by a certain
    # amount rather than set an entirely new value. Say we buy a used car and
    # put 100 miles on it between the time we buy it and the time we register
    # it. Here’s a method that allows us to pass this incremental amount and
    # add that value to the odometer reading:
    def increment_odometer(self, miles) :
        """ Add the given amount to the odometer reading. """
        if miles >= 0 :
            self.odometer_reading += miles
        else :
            print("You can't roll back an odometer!")
    
    def fill_gas_tank(self) :
        """ Print a statement indicating that the gas tank is full. """
        print("The gas tank is full.")


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Modifying an Attribute’s Value Directly
# The simplest way to modify the value of an attribute is to access
#  the attribute directly through an instance.
#  Here we set the odometer reading to 23 directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_new_car.update_odometer(10)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

class Battery() : 
    """ A simple attempt to model a battery for an electric car."""

    # At u we define a new class called Battery that doesn’t inherit from any
    # other class. The __init__() method at v has one parameter, battery_size,
    #  in addition to self. This is an optional parameter that sets the 
    # battery’s size to 70 if no value is provided.

    def __init__(self, battery_size=70) :
        """ Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self) :
        """ Print a statement describing the battery size. """
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    
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
    
    
    

    # You can override any method from the parent class that doesn’t fit what
    #you’re trying to model with the child class. To do this, you define a
    #  method in the child class with the same name as the method you want to
    #  override in the parent class. Python will disregard the parent class
    #  method and only pay attention to the method you define in the 
    # child class.
    def fill_gas_tank(self) :
        """ Electric cars don't have gas tanks. """
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()    
my_tesla.fill_gas_tank()