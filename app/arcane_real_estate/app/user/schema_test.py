from pytest import fixture
from .model import User
from .schema import ExistingUserSchema
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
def schema() -> ExistingUserSchema:
    return ExistingUserSchema()


def test_ExistingUserSchema_create(schema: ExistingUserSchema):
    assert schema


def test_ExistingUserSchema_works(schema: ExistingUserSchema, user_json: dict):
    params: UserInterface = schema.load(
        user_json
    )
    user = User(**params)

    assert user.user_id == 1
    assert user.first_name == "Test name"
    assert user.last_name == "Test description"
    assert user.mail == "user@user.user"
    assert user.birth_date == date_now
