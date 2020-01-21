from app.test.fixtures import app, db  # noqa
from flask_sqlalchemy import SQLAlchemy

from typing import List
from .model import Property
from .service import PropertyService  # noqa
from .interface import PropertyInterface


def test_get_all(db: SQLAlchemy):  # noqa
    yin: Property = Property(property_id=1, name="Yin", description="Test description")
    yang: Property = Property(property_id=2, name="Yaang", description="Test description")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    results: List[Property] = PropertyService.get_all()

    assert len(results) == 2
    assert yin in results and yang in results


def test_update(db: SQLAlchemy):  # noqa
    yin: Property = Property(property_id=1, name="Yin", description="Test description")

    db.session.add(yin)
    db.session.commit()
    updates = dict(name="Yang")

    PropertyService.update(yin, updates)

    result: Property = Property.query.get(yin.property_id)
    assert result.name == "Yang"


def test_delete_by_id(db: SQLAlchemy):  # noqa
    yin: Property = Property(property_id=1, name="Yin", description="Test description", city="berlin")
    yang: Property = Property(property_id=2, name="Yang", description="Test description", city="london")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    PropertyService.delete_by_id(1)
    results: List[Property] = Property.query.all()

    assert len(results) == 1
    assert yin not in results and yang in results


def test_create(db: SQLAlchemy):  # noqa

    yin: PropertyInterface = PropertyInterface(
        name="Yin", description="Test description", city="paris"
    )
    PropertyService.create(yin)
    results: List[Property] = Property.query.all()

    assert len(results) == 1

    for k in yin.keys():
        assert getattr(results[0], k) == yin[k]
