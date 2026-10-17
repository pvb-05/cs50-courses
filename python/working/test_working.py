import pytest
from working import convert

def test_convert():
    with pytest.raises(ValueError):
        convert('9:00 AM - 10:00 AM')
    with pytest.raises(ValueError):
        convert('13:00 AM to 10:00 AM')
    with pytest.raises(ValueError):
        convert('9:00 AM to 13:00 AM')
    with pytest.raises(ValueError):
        convert('9:60 AM to 10:00 AM')
    with pytest.raises(ValueError):
        convert('9:00 AM to 10:60 AM')
    assert convert('9:00 PM to 5:00 PM') == f'{21:02}:{0:02} to {17:02}:{0:02}'
    assert convert('12:00 PM to 5:00 PM') == f'{12:02}:{0:02} to {17:02}:{0:02}'
    assert convert('9:00 PM to 5:00 PM') == f'{21:02}:{0:02} to {17:02}:{0:02}'
    assert convert('9:00 PM to 12:00 PM') == f'{21:02}:{0:02} to {12:02}:{0:02}'
    assert convert('12:00 AM to 7:00 PM') == f'{0:02}:{0:02} to {19:02}:{0:02}'
    assert convert('9:00 AM to 7:00 PM') == f'{9:02}:{0:02} to {19:02}:{0:02}'
    assert convert('9:00 AM to 12:00 AM') == f'{9:02}:{0:02} to {0:02}:{0:02}'
    assert convert('9:00 AM to 11:00 AM') == f'{9:02}:{0:02} to {11:02}:{0:02}'
    assert convert('9 AM to 10 AM') == f'{9:02}:{0:02} to {10:02}:{0:02}'


