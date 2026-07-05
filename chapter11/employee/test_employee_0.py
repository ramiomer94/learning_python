from employee import Employee

def test_give_default_raise() :
    """Test if the $5000 default raise is give to the employee properly."""
    lakers_employee = Employee('austin', 'reaves', 10000)
    lakers_employee.give_raise()
    assert lakers_employee.salary == 15000

def test_give_custom_raise() :
    """
    Test whether a custom raise is added to the annual 
    salay of the employee properly
    """
    lakers_employee = Employee('austin', 'reaves', 10000)
    lakers_employee.give_raise(30000)
    assert lakers_employee.salary == 40000
