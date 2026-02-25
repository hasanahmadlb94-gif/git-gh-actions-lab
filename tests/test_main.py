from app.main import greet

def test_greet_name():
    assert greet("Hasan") == "Hello, Hasan!"

def test_greet_default():
    assert greet("") == "Hello, world!"
