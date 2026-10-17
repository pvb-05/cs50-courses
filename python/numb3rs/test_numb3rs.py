from numb3rs import validate


def test_vadilate():
    assert validate('cat') == False
    assert validate('512.0.0.0') == False
    assert validate('127.0.0.0.1') == False
    assert validate('127.0.0.1000') == False
    assert validate('127.0.0.1') == True
    assert validate('512.512.512.512') == False



