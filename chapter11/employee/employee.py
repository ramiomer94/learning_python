class Employee :
    """A simple class representing an employee"""

    def __init__ (self, first_name, last_name, salary) :
        """Store the employee first and last names and their annual salary"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    
    def give_raise(self,amount=5000) :
        """
        Give the employee an annual raise equal to amount (by default 5000)
        """
        self.salary += amount