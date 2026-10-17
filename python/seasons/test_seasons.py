from seasons import convert
import pytest

def test_convert():
    with pytest.raises(ValueError):
        convert('2005/11/15')
    with pytest.raises(ValueError):
        convert('2005-13-15')
    with pytest.raises(ValueError):
        convert('0000-11-15')
    with pytest.raises(ValueError):
        convert('2005-11-32')
    with pytest.raises(ValueError):
        convert('January 9th, 1997')
    with pytest.raises(ValueError):
        convert('2005-02-30')
    assert convert('2005-11-15') == 'Ten million, three hundred sixteen thousand, one hundred sixty minutes'
