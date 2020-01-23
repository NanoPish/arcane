from pytest import fixture

from .model import User
from .interface import UserInterface
import datetime

date_now = datetime.datetime.now().date()

@fixture
def interface() -> UserInterface:
    params: UserInterface = {
        "user_id": 0,
        "first_name": "test first name",
        "last_name": "test last name",
        "birth_date": date_now,
        "mail": "user@user.user",
    }
    return params


def test_UserInterface_create(interface: UserInterface):
    assert interface


def test_UserInterface_works(interface: UserInterface):
    assert User(**interface)
