from lib.gratitudes import *

def test_for_initial_empty_list():
    gratitudes = Gratitudes()
    result = gratitudes.format()
    assert result == "Be grateful for: "

def test_for_added_single_gratitude():
    gratitudes = Gratitudes()
    gratitudes.add("Good food")
    result = gratitudes.format()
    assert result == "Be grateful for: Good food"

def test_for_added_multiple_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("Good food")
    gratitudes.add('Warm bed')
    gratitudes.add('Good friends')
    result = gratitudes.format()
    assert result == "Be grateful for: Good food, Warm bed, Good friends"