from hello import gay

def test_gay():
    assert gay("gay") == True
    assert gay("not gay") == False

