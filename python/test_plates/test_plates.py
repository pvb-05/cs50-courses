# submit50 cs50/problems/2022/python/tests/plates
from plates import is_valid

def test_is_valid():
    assert is_valid('THISISCS50') == False
    assert is_valid('50CS') == False
    assert is_valid('C5CS') == False
    assert is_valid('5CCS') == False
    assert is_valid('CS50A') == False
    assert is_valid('CS05') == False
    assert is_valid("CS.50") == False
    assert is_valid("CS 50") == False
    assert is_valid("PI3.14") == False
    assert is_valid("1A") == False       # Sai vì bắt đầu bằng số (độ dài hợp lệ)
    assert is_valid("A1") == False       # Sai vì ký tự thứ 2 là số (độ dài hợp lệ)
    assert is_valid("12ABCD") == False
