from pytest import fixture
from flask_sqlalchemy import SQLAlchemy

from ..test.fixtures import app, db  # noqa
from .model import Room
from ..property.model_test import property
from ..property.model import Property
from ..type.model_test import type
from ..type.model import Type


@fixture
def room() -> Room:
    return Room(room_id=1, name="Test name", description="Test description", property_id=0)


def test_Room_create(room: Room):
    assert room


def test_Room_retrieve(room: Room, property: Property, type: Type, db: SQLAlchemy):  # noqa
    db.session.add(type)
    db.session.add(property)
    db.session.add(room)
    db.session.commit()
    s = Room.query.first()
    assert s.__dict__ == room.__dict__