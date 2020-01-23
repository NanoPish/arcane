from pytest import fixture
from .model import User
from .schema import UserSchema
from .interface import UserInterface
import datetime

date_now = datetime.datetime.now().date()


@fixture
def user_json() -> dict:
    return {
        "userId": 1,
        "firstName": "Test name",
        "lastName": "Test description",
        "mail": "user@user.user",
        "birthDate": str(date_now),
    }


@fixture
def schema() -> UserSchema:
    return UserSchema()


def test_UserSchema_create(schema: UserSchema):
    assert schema


def test_UserSchema_works(schema: UserSchema, user_json: dict):
    params: UserInterface = schema.load(
        user_json
    )
    user = User(**params)

    assert user.user_id == 1
    assert user.first_name == "Test name"
    assert user.last_name == "Test description"
    assert user.mail == "user@user.user"
    assert user.birth_date == date_now
