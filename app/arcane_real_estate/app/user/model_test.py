from pytest import fixture
from flask_sqlalchemy import SQLAlchemy
from ..test.fixtures import app, db  # noqa
from .model import User
import datetime

date_now = datetime.datetime.now().date()

@fixture
def user() -> User:
    return User(
        user_id=0,
        first_name="test first name",
        last_name="test last name",
        birth_date=date_now,
        mail="user@user.user",
        password_hash="sadf",
    )


def test_User_create(user: User):
    assert user


def test_User_retrieve(user: User, db: SQLAlchemy):  # noqa
    db.session.add(user)
    db.session.commit()
    s = User.query.first()
    assert s.__dict__ == user.__dict__
