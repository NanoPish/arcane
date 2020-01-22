from pytest import fixture
from flask_sqlalchemy import SQLAlchemy

from app.test.fixtures import app, db  # noqa
from .model import Room


@fixture
def room() -> Room:
    return Room(room_id=1, name="Test name", description="Test description")


def test_Room_create(room: Room):
    assert room


def test_Room_retrieve(room: Room, db: SQLAlchemy):  # noqa
    db.session.add(room)
    db.session.commit()
    s = Room.query.first()
    assert s.__dict__ == room.__dict__