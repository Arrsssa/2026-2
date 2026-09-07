from app import greet


def test_greet():
    assert greet("Arsalan") == "Hello, Arsalan! CI/CD deployment is working."


def test_empty_name():
    assert greet("") == "Please enter your name."
