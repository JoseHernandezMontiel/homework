import pytest
from src.users.model.user_model import User
from src.users.repository.user_repository import LocalUserRepository

@pytest.fixture
def test_user():
    return User(
        id=1,
        name='Joe',
        email="joe@gmail.com"
    )

def test_add_user(test_user):
    assert test_user is not None

    repository = LocalUserRepository()
    repository.add(test_user.name, test_user.email)

    assert repository.get(1) == test_user
    assert repository.get(1) is not None
    