from flask_sqlalchemy import SQLAlchemy
from typing import List
from ..test.fixtures import app, db  # noqa
from .model import Property
from .service import PropertyService  # noqa
from .interface import PropertyInterface
from ..type.model_test import type
from ..type.model import Type
from sqlalchemy import exc
import pytest

def get_test_property_0():
    return Property(property_id=0,
                    name="My nice house",
                    description='A red brick house',
                    city='Berlin',
                    type_id=0)


def get_test_property_1():
    return Property(property_id=1,
                    name="My nice pizza box",
                    description='Good quality cardboard, SF north',
                    city='San Francisco',
                    type_id=0)


def get_property_interface_0():
    return PropertyInterface(name="My nice house",
                             description='A red brick house',
                             city='Berlin',
                             type_id=0)


def test_get_all(db: SQLAlchemy, type: Type):  # noqa
    property_0 = get_test_property_0()
    property_1 = get_test_property_1()

    db.session.add(type)
    db.session.add(property_0)
    db.session.add(property_1)

    db.session.commit()

    results: List[Property] = PropertyService.get_all()

    assert len(results) == 2
    assert property_0 in results and property_1 in results


def test_update(db: SQLAlchemy, type: Type):  # noqa
    # TODO test all fields
    property_0 = get_test_property_0()

    db.session.add(type)
    db.session.add(property_0)
    db.session.commit()

    updates: PropertyInterface = dict(name='New name')
    PropertyService.update(property_0, updates)

    result: Property = Property.query.get(property_0.property_id)
    assert result.name == 'New name'


def test_delete_by_id(db: SQLAlchemy, type: Type):  # noqa
    property_0 = get_test_property_0()
    property_1 = get_test_property_1()

    db.session.add(type)
    db.session.add(property_0)
    db.session.add(property_1)

    db.session.commit()

    PropertyService.delete_by_id(property_1.property_id)
    db.session.commit()

    results: List[Property] = Property.query.all()

    assert len(results) == 1
    assert property_1 not in results and property_0 in results


def test_create(db: SQLAlchemy, type: Type):  # noqa
    property_interface: PropertyInterface = get_property_interface_0()

    db.session.add(type)
    PropertyService.create(property_interface)

    results: List[Property] = Property.query.all()

    assert len(results) == 1

    for k in property_interface.keys():
        assert getattr(results[0], k) == property_interface[k]

def test_create_dont_respect_foreign_keys(db: SQLAlchemy, type: Type):  # noqa
    property_interface: PropertyInterface = get_property_interface_0()
    property_interface["type_id"] = 2354

    db.session.add(type)
    try:
        PropertyService.create(property_interface)
    except exc.IntegrityError:
        assert True == True
        return True

    pytest.fail("Did not trow integrity error")