from app import db  # noqa
from typing import List
from werkzeug.exceptions import BadRequest, Conflict, Unauthorized, NotFound
from flask import jsonify
from flask_jwt_extended import create_access_token
from datetime import timedelta
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
    def get_user_id_by_user_mail(mail: str) -> int:
        return User.query.filter_by(mail=mail).first().user_id


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
        try:
            new_user = User(
                first_name=new_attrs["first_name"],
                last_name=new_attrs["last_name"],
                birth_date=new_attrs["birth_date"],
                mail=new_attrs["mail"],
            )
            mail = new_attrs['mail']
            password = new_attrs['password']
        except KeyError:
            raise BadRequest()

        if User.query.filter_by(mail=mail).first() is not None:
            raise Conflict("Existing mail")

        new_user.hash_password(password)

        db.session.add(new_user)
        db.session.commit()

        return new_user

    @staticmethod
    def authenticate(mail: str, password: str) -> dict:
        user: User = User.query.filter_by(mail=mail).first()

        if user is None:
            raise NotFound

        if user.verify_password(password):
            access_token = create_access_token(identity=mail, expires_delta=timedelta(days=1))
            return jsonify(access_token=access_token)
        else:
            raise Unauthorized
