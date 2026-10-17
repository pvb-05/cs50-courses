from um import count

def test_count():
    assert count(' um ') == 1
    assert count('UM') == 1
    assert count('Hello, um') == 1
    assert count('Hello') == 0
    assert count('YumYum') == 0
    assert count('um, hello, um, YumYum') == 2
