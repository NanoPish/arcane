from typing import List
from werkzeug.exceptions import BadRequest, Conflict

from app import db  # noqa
from .model import User
from .interface import UserInterface


class UserService:
    @staticmethod
    def get_all() -> List[User]:
        return User.query.all()

    @staticmethod
    def get_by_id(user_id: int) -> User:
        return User.query.get(user_id)

    @staticmethod
    def update(user: User, user_change_updates: UserInterface) -> User:
        user.update(user_change_updates)
        db.session.commit()
        return user

    @staticmethod
    def delete_by_id(user_id: int) -> List[int]:
        user = User.query.filter(User.user_id == user_id).first()
        if not user:
            return []
        db.session.delete(user)
        db.session.commit()
        return [user_id]

    @staticmethod
    def create(new_attrs: UserInterface) -> User:
        new_user = User(
            first_name=new_attrs["first_name"],
            last_name=new_attrs["last_name"],
            birth_date=new_attrs["birth_date"],
            mail=new_attrs["mail"],
        )

        mail = new_attrs['mail']
        password = new_attrs['password']

        if mail is None or password is None:
            raise BadRequest()

        if User.query.filter_by(mail=mail).first() is not None:
            raise Conflict()

        new_user.hash_password(password)

        db.session.add(new_user)
        db.session.commit()

        return new_user
