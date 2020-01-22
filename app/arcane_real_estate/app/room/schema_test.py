from pytest import fixture

from .model import Room
from .schema import RoomSchema
from .interface import RoomInterface


@fixture
def schema() -> RoomSchema:
    return RoomSchema()


def test_RoomSchema_create(schema: RoomSchema):
    assert schema


def test_RoomSchema_works(schema: RoomSchema):
    params: RoomInterface = schema.load(
        {"roomId": 1, "name": "Test name", "description": "Test description"}
    )
    room = Room(**params)

    assert room.room_id == 1
    assert room.name == "Test name"
    assert room.description == "Test description"
