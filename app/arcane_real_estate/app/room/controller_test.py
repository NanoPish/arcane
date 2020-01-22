from unittest.mock import patch
from flask.testing import FlaskClient
from flask.wrappers import Response

from app.test.fixtures import client, app  # noqa
from .model import Room
from .schema import RoomSchema
from .service import RoomService
from .interface import RoomInterface


def room(id: int = 123, name: str = "Test name") -> Room:
    return Room(room_id=id, name="Test name", description="Test description")


class TestRoomResource:
    @patch.object(RoomService, "get_all", lambda: [room(123), room(456)])
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results = client.get("/api/room", follow_redirects=True).get_json()
            expected = RoomSchema(many=True).dump([room(456), room(123)])
            for r in results:
                assert r in expected


class TestRoomRoomResource:
    @patch.object(
        RoomService,
        "get_all",
        lambda: [room(123, name="Test name 1"), room(456, name="Test name 2")],
    )
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results: dict = client.get("/api/room", follow_redirects=True).get_json()
            expected = (
                RoomSchema(many=True)
                .dump([room(123, name="Test name 1"), room(456, name="Test name 2")])

            )
            for r in results:
                assert r in expected

    @patch.object(
        RoomService,
        "create",
        lambda create_request: Room(
            name=create_request["name"],
            description=create_request["description"],
        ),
    )
    def test_post(self, client: FlaskClient):  # noqa
        with client:

            payload = dict(name="Test name", description="Test description")
            result: dict = client.post("/api/room/", json=payload).get_json()
            expected = (
                RoomSchema()
                .dump(Room(name=payload["name"], description=payload["description"]))

            )
            assert result == expected


def fake_update(room: Room, changes: RoomInterface) -> Room:
    # To fake an update, just return a new object
    updated_room = Room(room_id=room.room_id, name=changes["name"])
    return updated_room


class TestRoomRoomIdResource:
    @patch.object(RoomService, "get_by_id", lambda id: Room(room_id=id))
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            result: dict = client.get("/api/room/123").get_json()
            expected = Room(room_id=123)
            assert result["roomId"] == expected.room_id

    @patch.object(RoomService, "delete_by_id", lambda id: [id])
    def test_delete(self, client: FlaskClient):  # noqa
        with client:
            result: dict = client.delete("/api/room/123").get_json()
            expected = dict(status="Success", id=[123])
            assert result == expected

    @patch.object(RoomService, "get_by_id", lambda id: Room(room_id=id))
    @patch.object(RoomService, "update", fake_update)
    def test_put(self, client: FlaskClient):  # noqa
        with client:
            result: dict = client.put(
                "/api/room/123", json={"name": "New name"}
            ).get_json()
            expected: dict = RoomSchema().dump(
                Room(room_id=123, name="New name")
            )
            assert result == expected