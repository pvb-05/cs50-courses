# submit50 cs50/problems/2022/python/tests/twttr
from twttr import shorten

def test_shorten():
    assert shorten('Twitter') == 'Twttr'
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten('CS50') == 'CS50'
    assert shorten('AEIOU') == ''
    assert shorten('HELLO, WORLD') == 'HLL, WRLD'

