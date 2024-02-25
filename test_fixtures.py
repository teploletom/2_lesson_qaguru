import pytest

@pytest.fixture()
def browser():
    print("1")

@pytest.fixture()
def login_page(browser):
    print("2")

@pytest.fixture()
def user():
    print("3")
    return "username", "password"

def test_login(user):
    username, password = user
    assert username == "username"
    assert password == "password"
