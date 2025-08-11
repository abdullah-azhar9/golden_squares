from lib.counter import *

def test_counter_is_correct():
    counter = Counter()
    counter.add(5)
    counter.add(3)
    result = counter.report()
    assert result == "Counted to 8 so far."