from src.math_operations import add, sub

def test_add():
    assert add(2, 3) == 5
    assert add(2, -3) == -1
    assert add(4, 4) == 8

def test_sub():
    assert sub(2, 3) == -1
    assert sub(5, 5) == 0
    assert sub(3, 2) == 1