from app.test.fixtures import app, db  # noqa
from flask_sqlalchemy import SQLAlchemy

from typing import List
from .model import User
from .service import UserService  # noqa
from .interface import UserInterface


def test_get_all(db: SQLAlchemy):  # noqa
    yin: User = User(user_id=1, name="Yin", description="Test description")
    yang: User = User(user_id=2, name="Yaang", description="Test description")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    results: List[User] = UserService.get_all()

    assert len(results) == 2
    assert yin in results and yang in results


def test_update(db: SQLAlchemy):  # noqa
    yin: User = User(user_id=1, name="Yin", description="Test description")

    db.session.add(yin)
    db.session.commit()

    result: User = User.query.get(yin.user_id)
    assert result.name == "Yin"

    updates = dict(name="Yang")
    UserService.update(yin, updates)

    result: User = User.query.get(yin.user_id)
    assert result.name == "Yang"


def test_delete_by_id(db: SQLAlchemy):  # noqa
    yin: User = User(user_id=1, name="Yin", description="Test description")
    yang: User = User(user_id=2, name="Yang", description="Test description")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    UserService.delete_by_id(1)
    results: List[User] = User.query.all()

    assert len(results) == 1
    assert yin not in results and yang in results


def test_create(db: SQLAlchemy):  # noqa

    yin: UserInterface = UserInterface(
        user_id=1, name="Yin", description="Test description"
    )
    UserService.create(yin)
    results: List[User] = User.query.all()

    assert len(results) == 1

    for k in yin.keys():
        assert getattr(results[0], k) == yin[k]
