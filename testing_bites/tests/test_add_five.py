from lib.add_five import *

#function name must start with test_ for pytest to find it.
#the test of the function should describe what the test verifies.
def test_add_five_returns_eight_for_three():
    result = add_five(3)
    assert result == 8