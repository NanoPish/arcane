from unittest.mock import patch
from flask.testing import FlaskClient
from flask.wrappers import Response

from app.test.fixtures import client, app  # noqa
from .model import Property
from .schema import PropertySchema
from .service import PropertyService
from .interface import PropertyInterface


def property(id: int = 123, name: str = "Test name") -> Property:
    return Property(property_id=id, name="Test name", description="Test description")


class TestPropertyResource:
    @patch.object(PropertyService, "get_all", lambda: [property(123), property(456)])
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results = client.get("/api/property", follow_redirects=True).get_json()
            expected = PropertySchema(many=True).dump([property(456), property(123)])
            for r in results:
                assert r in expected


class TestPropertyPropertyResource:
    @patch.object(
        PropertyService,
        "get_all",
        lambda: [property(123, name="Test name 1"), property(456, name="Test name 2")],
    )
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results: dict = client.get("/api/property", follow_redirects=True).get_json()
            expected = (
                PropertySchema(many=True)
                .dump([property(123, name="Test name 1"), property(456, name="Test name 2")])
            )
            for r in results:
                assert r in expected

    @patch.object(
        PropertyService,
        "create",
        lambda create_request: Property(
            name=create_request["name"],
            description=create_request["description"],
        ),
    )
    def test_post(self, client: FlaskClient):  # noqa
        with client:

            payload = dict(name="Test name", description="Test description")
            result: dict = client.post("/api/property/", json=payload).get_json()
            expected = (
                PropertySchema()
                .dump(Property(name=payload["name"], description=payload["description"]))
            )
            print("result", result)
            assert result == expected


def fake_update(property: Property, changes: PropertyInterface) -> Property:
    # To fake an update, just return a new object
    updated_property = Property(property_id=property.property_id, name=changes["name"])
    return updated_property


class TestPropertyPropertyIdResource:
    @patch.object(PropertyService, "get_by_id", lambda id: Property(property_id=id))
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            result: dict = client.get("/api/property/123").get_json()
            expected = Property(property_id=123)
            assert result["propertyId"] == expected.property_id

    @patch.object(PropertyService, "delete_by_id", lambda id: [id])
    def test_delete(self, client: FlaskClient):  # noqa
        with client:
            result: dict = client.delete("/api/property/123").get_json()
            expected = dict(status="Success", id=[123])
            assert result == expected

    @patch.object(PropertyService, "get_by_id", lambda id: Property(property_id=id))
    @patch.object(PropertyService, "update", fake_update)
    def test_put(self, client: FlaskClient):  # noqa
        with client:
            result: dict = client.put(
                "/api/property/123", json={"name": "New name"}
            ).get_json()
            expected: dict = PropertySchema().dump(
                Property(property_id=123, name="New name")
            )
            assert result == expected