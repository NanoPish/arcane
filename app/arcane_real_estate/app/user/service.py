from typing import List

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
            user_id=new_attrs["user_id"],
            name=new_attrs["name"],
            description=new_attrs["description"],
        )

        db.session.add(new_user)
        db.session.commit()

        return new_user
