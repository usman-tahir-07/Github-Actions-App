from src.math_operations import add, sub

def add_test():
    assert add(2, 3) == 5
    assert add(2, -3) == -1
    assert add(4, 4) == 8

def sub_test():
    assert sub(2, 3) == -1
    assert sub(5, 5) == 0
    assert sub(3, 2) == 1