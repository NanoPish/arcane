from app.test.fixtures import app, db  # noqa
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest, Conflict, Unauthorized, NotFound
from typing import List
from .model import User
from .service import UserService  # noqa
from .interface import UserInterface
import datetime
from werkzeug.exceptions import BadRequest, Conflict
import pytest

date_now = datetime.datetime.now().date()


def get_test_user_0():
    return User(
        first_name="A user firstname",
        last_name="A user lastname",
        birth_date=date_now,
        mail="user@user.user",
        password_hash="asdf",
    )


def get_test_user_1():
    return User(
        first_name="Another firstname",
        last_name="Another lastname",
        birth_date=date_now,
        mail="user2@user.user",
        password_hash="asdf",
    )


def get_user_interface_0():
    return UserInterface(
        first_name="A user firstname",
        last_name="A user lastname",
        birth_date=date_now,
        mail="user@user.user",
        password="1111111",
    )


def test_get_all(db: SQLAlchemy):  # noqa
    yin = get_test_user_0()
    yang = get_test_user_1()
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    results: List[User] = UserService.get_all()

    assert len(results) == 2
    assert yin in results and yang in results


def test_update(db: SQLAlchemy):  # noqa
    yin = get_test_user_0()

    db.session.add(yin)
    db.session.commit()

    result: User = User.query.get(yin.user_id)
    assert result.first_name == yin.first_name

    updates = dict(first_name="Yang")
    UserService.update(yin, updates)

    result: User = User.query.get(yin.user_id)
    assert result.first_name == "Yang"


def test_delete_by_id(db: SQLAlchemy):  # noqa
    yin = get_test_user_0()
    yang = get_test_user_1()
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    UserService.delete_by_id(1)
    results: List[User] = User.query.all()

    assert len(results) == 1
    assert yin not in results and yang in results


def test_create(db: SQLAlchemy):  # noqa
    yin: UserInterface = get_user_interface_0()
    UserService.create(yin)
    results: List[User] = User.query.all()

    assert len(results) == 1
    del yin['password']
    for k in yin.keys():
        assert getattr(results[0], k) == yin[k]


def test_create_duplicate_mail(db: SQLAlchemy):  # noqa
    yin: UserInterface = get_user_interface_0()
    UserService.create(yin)
    try:
        UserService.create(yin)
    except Conflict:
        db.session.rollback()
        results: List[User] = User.query.all()
        assert len(results) == 1
        del yin['password']
        for k in yin.keys():
            assert getattr(results[0], k) == yin[k]
        return 0

    assert True is False


@pytest.mark.parametrize("missing", ['password', 'mail', 'first_name'])
def test_create_no_password(db: SQLAlchemy, missing):  # noqa
    yin: UserInterface = get_user_interface_0()
    del yin[missing]
    try:
        UserService.create(yin)
    except BadRequest:
        db.session.rollback()
        results: List[User] = User.query.all()
        assert len(results) == 0
        return 0

    assert True is False


def test_authenticate(db: SQLAlchemy):  # noqa
    yin: UserInterface = get_user_interface_0()
    UserService.create(yin)
    results: List[User] = User.query.all()

    assert len(results) == 1
    user: User = results[0]
    assert user.verify_password(yin["password"]) is True
    try:
        UserService.authenticate(yin["mail"], yin["password"])
        return 0
    except Unauthorized:
        assert True is False
