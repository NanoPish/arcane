from pytest import fixture

from .model import Room
from .interface import RoomInterface


@fixture
def interface() -> RoomInterface:

    params: RoomInterface = {
        "room_id": 1,
        "name": "Test name",
        "description": "Test description",
    }
    return params


def test_RoomInterface_create(interface: RoomInterface):
    assert interface


def test_RoomInterface_works(interface: RoomInterface):
    assert Room(**interface)