from pytest import fixture
from flask_sqlalchemy import SQLAlchemy
from ..type.model_test import type
from ..type.model import Type
from app.test.fixtures import app, db  # noqa
from .model import Property


@fixture
def property() -> Property:
    return Property(property_id=0, name="Test name", description="Test description", city="berlin", type_id=0)


def test_Property_create(property: Property):
    assert property


def test_Property_retrieve(property: Property, type: Type, db: SQLAlchemy):  # noqa
    db.session.add(type)
    db.session.add(property)
    db.session.commit()
    s = Property.query.first()
    assert s.__dict__ == property.__dict__