from pytest import fixture

from .model import User
from .schema import UserSchema
from .interface import UserInterface


@fixture
def schema() -> UserSchema:
    return UserSchema()


def test_UserSchema_create(schema: UserSchema):
    assert schema


def test_UserSchema_works(schema: UserSchema):
    params: UserInterface = schema.load(
        {"userId": 1, "name": "Test name", "description": "Test description"}
    )
    user = User(**params)

    assert user.user_id == 1
    assert user.name == "Test name"
    assert user.description == "Test description"
