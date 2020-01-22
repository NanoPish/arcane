from flask_sqlalchemy import SQLAlchemy
from typing import List
from app.test.fixtures import app, db  # noqa
from .model import Property
from .service import PropertyService  # noqa
from .interface import PropertyInterface


def get_test_property_0():
    return Property(property_id=0, name="My nice house", description='A red brick house', city='Berlin', type_id=0)

def get_test_property_1():
    return Property(property_id=1, name="My nice pizza box", description='Good quality cardboard, SF north', city='San Francisco', type_id=1)

def get_property_interface_0():
    return PropertyInterface(name="My nice house", description='A red brick house', city='Berlin', type_id=0)

def test_get_all(db: SQLAlchemy):  # noqa
    db.session.add(get_test_property_0())
    db.session.add(get_test_property_1())

    db.session.commit()

    results: List[Property] = PropertyService.get_all()

    assert len(results) == 2
    assert get_test_property_0() in results and get_test_property_1() in results


def test_update(db: SQLAlchemy):  # noqa
    db.session.add(get_test_property_0())
    db.session.commit()

    updates: PropertyInterface = dict(name='New name')
    PropertyService.update(get_test_property_0(), updates)

    result: Property = Property.query.get(get_test_property_0().property_id)
    assert result.name == 'New name' #test update all fields


def test_delete_by_id(db: SQLAlchemy):  # noqa
    db.session.add(get_test_property_0())
    db.session.add(get_test_property_1())

    db.session.commit()

    WidgetService.delete_by_id(get_test_property_1().property_id)
    db.session.commit()

    results: List[Property] = Property.query.all()

    assert len(results) == 1
    assert yin not in results and yang in results


def test_create(db: SQLAlchemy):  # noqa
    PropertyService.create(get_property_interface_0())

    results: List[Property] = Property.query.all()

    assert len(results) == 1

    for k in get_property_interface_0().keys():
        assert getattr(results[0], k) == get_property_interface_0()[k]
