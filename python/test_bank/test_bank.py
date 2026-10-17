# submit50 cs50/problems/2022/python/tests/bank
from bank import value

def test_value():
    assert value('hello') == 0
    assert value('hi') == 20
    assert value('goodbye') == 100
    assert value('Hello') == 0

