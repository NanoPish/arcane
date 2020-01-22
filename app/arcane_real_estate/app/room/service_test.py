from app.test.fixtures import app, db  # noqa
from flask_sqlalchemy import SQLAlchemy

from typing import List
from .model import Room
from .service import RoomService  # noqa
from .interface import RoomInterface


def test_get_all(db: SQLAlchemy):  # noqa
    yin: Room = Room(room_id=1, name="Yin", description="Test description")
    yang: Room = Room(room_id=2, name="Yaang", description="Test description")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    results: List[Room] = RoomService.get_all()

    assert len(results) == 2
    assert yin in results and yang in results


def test_update(db: SQLAlchemy):  # noqa
    yin: Room = Room(room_id=1, name="Yin", description="Test description")

    db.session.add(yin)
    db.session.commit()

    result: Room = Room.query.get(yin.room_id)
    assert result.name == "Yin"

    updates = dict(name="Yang")
    RoomService.update(yin, updates)

    result: Room = Room.query.get(yin.room_id)
    assert result.name == "Yang"


def test_delete_by_id(db: SQLAlchemy):  # noqa
    yin: Room = Room(room_id=1, name="Yin", description="Test description")
    yang: Room = Room(room_id=2, name="Yang", description="Test description")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    RoomService.delete_by_id(1)
    results: List[Room] = Room.query.all()

    assert len(results) == 1
    assert yin not in results and yang in results


def test_create(db: SQLAlchemy):  # noqa

    yin: RoomInterface = RoomInterface(
        room_id=1, name="Yin", description="Test description"
    )
    RoomService.create(yin)
    results: List[Room] = Room.query.all()

    assert len(results) == 1

    for k in yin.keys():
        assert getattr(results[0], k) == yin[k]
