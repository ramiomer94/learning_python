import pytest
from employee import Employee

@pytest.fixture
def lakers_employee() :
    """An instance of Employee representing Lakers employee Austin Reaves """
    lakers_employee = Employee('austin', 'reaves', 10000)
    return lakers_employee

def test_give_default_raise(lakers_employee) :
    """Test if the $5000 default raise is give to the employee properly."""
    lakers_employee.give_raise()
    assert lakers_employee.salary == 15000

def test_give_custom_raise(lakers_employee) :
    """
        Test whether a custom raise is added to the annual 
        salay of the employee properly
    """
    lakers_employee.give_raise(amount=2000)
    assert lakers_employee.salary == 12000
     

