# submit50 cs50/problems/2022/python/tests/fuel
import pytest
from fuel import convert, gauge

def test_convert_correct():
    assert convert('3/4')

def test_convert_value_error():
    with pytest.raises(ValueError):
        convert('s/s')
    with pytest.raises(ValueError):
        convert('5/4')
    with pytest.raises(ValueError):
        convert('5/s')
    with pytest.raises(ValueError):
        convert('s/5')

def test_convert_round():
  # Kiểm tra một trường hợp đơn giản
    assert convert("1/2") == 50

    # Kiểm tra trường hợp cần làm tròn xuống
    assert convert("1/3") == 33

    # Kiểm tra trường hợp cần làm tròn lên
    assert convert("2/3") == 67

def test_convert_zero_error():
    with pytest.raises(ZeroDivisionError):
        convert('5/0')

def test_gauge():
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
    assert gauge(55) == f'55%'

