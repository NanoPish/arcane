from unittest.mock import patch
from flask.testing import FlaskClient
from flask.wrappers import Response

from app.test.fixtures import client, app  # noqa
from .model import User
from .schema import UserSchema
from .service import UserService
from .interface import UserInterface


def user(id: int = 123, name: str = "Test name") -> User:
    return User(user_id=id, name="Test name", description="Test description")


class TestUserResource:
    @patch.object(UserService, "get_all", lambda: [user(123), user(456)])
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results = client.get("/api/user", follow_redirects=True).get_json()
            expected = UserSchema(many=True).dump([user(456), user(123)])
            for r in results:
                assert r in expected


class TestUserUserResource:
    @patch.object(
        UserService,
        "get_all",
        lambda: [user(123, name="Test name 1"), user(456, name="Test name 2")],
    )
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results: dict = client.get("/api/user", follow_redirects=True).get_json()
            expected = (
                UserSchema(many=True)
                .dump([user(123, name="Test name 1"), user(456, name="Test name 2")])

            )
            for r in results:
                assert r in expected

    @patch.object(
        UserService,
        "create",
        lambda create_request: User(
            name=create_request["name"],
            description=create_request["description"],
        ),
    )
    def test_post(self, client: FlaskClient):  # noqa
        with client:

            payload = dict(name="Test name", description="Test description")
            result: dict = client.post("/api/user/", json=payload).get_json()
            expected = (
                UserSchema()
                .dump(User(name=payload["name"], description=payload["description"]))

            )
            assert result == expected


def fake_update(user: User, changes: UserInterface) -> User:
    # To fake an update, just return a new object
    updated_user = User(user_id=user.user_id, name=changes["name"])
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
                "/api/user/123", json={"name": "New name"}
            ).get_json()
            expected: dict = UserSchema().dump(
                User(user_id=123, name="New name")
            )
            assert result == expected