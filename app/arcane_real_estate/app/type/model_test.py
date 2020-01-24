from pytest import fixture
from flask_sqlalchemy import SQLAlchemy

from ...app.test.fixtures import app, db  # noqa
from .model import Type


@fixture
def type() -> Type:
    return Type(type_id=0, name="Test name", description="Test description")


def test_Type_create(type: Type):
    assert type


def test_Type_retrieve(type: Type, db: SQLAlchemy):  # noqa
    db.session.add(type)
    db.session.commit()
    s = Type.query.first()
    assert s.__dict__ == type.__dict__