from app import add, greet

def test_add():
    assert add(2, 3) == 98

def test_greet():
    assert greet("World") == "Hello, World!"
