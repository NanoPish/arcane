from unittest.mock import patch
from flask.testing import FlaskClient
import datetime

from app.test.fixtures import client, app  # noqa
from .model import User
from .schema import UserSchema
from .service import UserService
from .interface import UserInterface


date_now = datetime.datetime.now().date()

def existing_user(id: int, first_name: str = "Test first name") -> User:
    return User(user_id=id,
                first_name=first_name,
                last_name="Test last name",
                mail="user@user.user",
                birth_date=date_now)


class TestUserResource:
    @patch.object(UserService, "get_all", lambda: [existing_user(123), existing_user(456)])
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results = client.get("/api/user", follow_redirects=True).get_json()
            expected = UserSchema(many=True).dump([existing_user(456), existing_user(123)])
            for r in results:
                assert r in expected


class TestUserUserResource:
    @patch.object(
        UserService,
        "get_all",
        lambda: [existing_user(123, first_name="Test first name 1"), existing_user(456, first_name="Test first name 2")],
    )
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results: dict = client.get("/api/user", follow_redirects=True).get_json()
            expected = (
                UserSchema(many=True)
                    .dump([existing_user(123, first_name="Test first name 1"), existing_user(456, first_name="Test first name 2")])

            )
            for r in results:
                assert r in expected

    @patch.object(
        UserService,
        "create",
        lambda create_request: User(
            first_name=create_request["first_name"],
            last_name=create_request["last_name"],
            birth_date=create_request["birth_date"],
            mail=create_request["mail"],
        ),
    )
    def test_post(self, client: FlaskClient):  # noqa
        with client:
            payload = dict(
                firstName="Test first name",
                lastName="Test last name",
                birthDate=str(date_now),
                mail="user@user.user",
            )
            result: dict = client.post("/api/user/", json=payload).get_json()
            expected = (
                UserSchema()
                    .dump(User(
                    first_name=payload["firstName"],
                    last_name=payload["lastName"],
                    birth_date=date_now,
                    mail=payload["mail"],
                ))

            )
            assert result == expected


def fake_update(user: User, changes: UserInterface) -> User:
    # To fake an update, just return a new object
    updated_user = User(user_id=user.user_id, first_name=changes["first_name"])
    return updated_user


class TestUserUserIdResource:
    @patch.object(UserService, "get_by_id", lambda id: User(user_id=id))
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            result: dict = client.get("/api/user/123").get_json()
            expected = User(user_id=123)
            assert result["userId"] == expected.user_id

    @patch.object(UserService, "delete_by_id", lambda id: [id])
    def test_delete(self, client: FlaskClient):  # noqa
        with client:
            result: dict = client.delete("/api/user/123").get_json()
            expected = dict(status="Success", id=[123])
            assert result == expected

    @patch.object(UserService, "get_by_id", lambda id: User(user_id=id))
    @patch.object(UserService, "update", fake_update)
    def test_put(self, client: FlaskClient):  # noqa
        with client:
            result: dict = client.put(
                "/api/user/123", json={"firstName": "New name"}
            ).get_json()
            expected: dict = UserSchema().dump(
                User(user_id=123, first_name="New name")
            )
            assert result == expected
