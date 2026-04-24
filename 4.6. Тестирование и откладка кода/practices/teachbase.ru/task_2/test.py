from main import add


def test_example():
    assert add(2, 3) == 5
    assert add(15, 7) == 22
    assert add(16, 3.0) == 19.0

def test_add_zero():
    assert add(5, 0) == 5

def test_minus():
    assert add(-50, -5) == -55
    