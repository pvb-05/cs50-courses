from jar import Jar
import pytest

def test_init():
    with pytest.raises(ValueError):
        jars = Jar(0)
    jars = Jar()
    assert jars.capacity == 12
    assert jars.size == 0

def test_str():
    jars = Jar()
    assert jars.__str__() == ""
    jars.deposit(1)
    assert jars.__str__() == "🍪"

def test_deposit():
    jars = Jar()
    jars.deposit(1)
    assert jars.size == 1
    with pytest.raises(ValueError):
        jars.deposit(13)

def test_with_draw():
    jars = Jar()
    with pytest.raises(ValueError):
        jars.withdraw(1)
    jars.deposit(2)
    jars.withdraw(1)
    assert jars.size == 1
