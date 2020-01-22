from unittest.mock import patch
from flask.testing import FlaskClient
from flask.wrappers import Response

from app.test.fixtures import client, app  # noqa
from .model import Type
from .schema import TypeSchema
from .service import TypeService
from .interface import TypeInterface


def type(id: int = 123, name: str = "Test name") -> Type:
    return Type(type_id=id, name="Test name", description="Test description")


class TestTypeResource:
    @patch.object(TypeService, "get_all", lambda: [type(123), type(456)])
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results = client.get("/api/type", follow_redirects=True).get_json()
            expected = TypeSchema(many=True).dump([type(456), type(123)])
            for r in results:
                assert r in expected


class TestTypeTypeResource:
    @patch.object(
        TypeService,
        "get_all",
        lambda: [type(123, name="Test name 1"), type(456, name="Test name 2")],
    )
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results: dict = client.get("/api/type", follow_redirects=True).get_json()
            expected = (
                TypeSchema(many=True)
                .dump([type(123, name="Test name 1"), type(456, name="Test name 2")])

            )
            for r in results:
                assert r in expected

    @patch.object(
        TypeService,
        "create",
        lambda create_request: Type(
            name=create_request["name"],
            description=create_request["description"],
        ),
    )
    def test_post(self, client: FlaskClient):  # noqa
        with client:

            payload = dict(name="Test name", description="Test description")
            result: dict = client.post("/api/type/", json=payload).get_json()
            expected = (
                TypeSchema()
                .dump(Type(name=payload["name"], description=payload["description"]))

            )
            assert result == expected


def fake_update(type: Type, changes: TypeInterface) -> Type:
    # To fake an update, just return a new object
    updated_type = Type(type_id=type.type_id, name=changes["name"])
    return updated_type


class TestTypeTypeIdResource:
    @patch.object(TypeService, "get_by_id", lambda id: Type(type_id=id))
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            result: dict = client.get("/api/type/123").get_json()
            expected = Type(type_id=123)
            assert result["typeId"] == expected.type_id

    @patch.object(TypeService, "delete_by_id", lambda id: [id])
    def test_delete(self, client: FlaskClient):  # noqa
        with client:
            result: dict = client.delete("/api/type/123").get_json()
            expected = dict(status="Success", id=[123])
            assert result == expected

    @patch.object(TypeService, "get_by_id", lambda id: Type(type_id=id))
    @patch.object(TypeService, "update", fake_update)
    def test_put(self, client: FlaskClient):  # noqa
        with client:
            result: dict = client.put(
                "/api/type/123", json={"name": "New name"}
            ).get_json()
            expected: dict = TypeSchema().dump(
                Type(type_id=123, name="New name")
            )
            assert result == expected