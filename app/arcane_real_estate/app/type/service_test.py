from app.test.fixtures import app, db  # noqa
from flask_sqlalchemy import SQLAlchemy

from typing import List
from .model import Type
from .service import TypeService  # noqa
from .interface import TypeInterface


def test_get_all(db: SQLAlchemy):  # noqa
    yin: Type = Type(type_id=1, name="Yin", description="Test description")
    yang: Type = Type(type_id=2, name="Yaang", description="Test description")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    results: List[Type] = TypeService.get_all()

    assert len(results) == 2
    assert yin in results and yang in results


def test_update(db: SQLAlchemy):  # noqa
    yin: Type = Type(type_id=1, name="Yin", description="Test description")

    db.session.add(yin)
    db.session.commit()

    result: Type = Type.query.get(yin.type_id)
    assert result.name == "Yin"

    updates = dict(name="Yang")
    TypeService.update(yin, updates)

    result: Type = Type.query.get(yin.type_id)
    assert result.name == "Yang"


def test_delete_by_id(db: SQLAlchemy):  # noqa
    yin: Type = Type(type_id=1, name="Yin", description="Test description")
    yang: Type = Type(type_id=2, name="Yang", description="Test description")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    TypeService.delete_by_id(1)
    results: List[Type] = Type.query.all()

    assert len(results) == 1
    assert yin not in results and yang in results


def test_create(db: SQLAlchemy):  # noqa

    yin: TypeInterface = TypeInterface(
        type_id=1, name="Yin", description="Test description"
    )
    TypeService.create(yin)
    results: List[Type] = Type.query.all()

    assert len(results) == 1

    for k in yin.keys():
        assert getattr(results[0], k) == yin[k]
