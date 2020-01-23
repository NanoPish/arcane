from pytest import fixture

from .model import User
from .interface import UserInterface


@fixture
def interface() -> UserInterface:

    params: UserInterface = {
        "user_id": 1,
        "name": "Test name",
        "description": "Test description",
    }
    return params


def test_UserInterface_create(interface: UserInterface):
    assert interface


def test_UserInterface_works(interface: UserInterface):
    assert User(**interface)