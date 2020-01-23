from flask_restplus import Resource
from flask import request
from flask_restplus import Namespace
from flask_accepts import accepts, responds
from flask.wrappers import Response
from typing import List

from .schema import ExistingUserSchema
from .schema import NewUserSchema
from .model import User
from .service import UserService

api = Namespace("User", description="User management")


@api.route("/")
class UserResource(Resource):
    """Users"""

    @responds(schema=ExistingUserSchema, many=True)
    def get(self) -> List[User]:
        """Get all Users"""

        return UserService.get_all()

    @accepts(schema=NewUserSchema, api=api)
    @responds(schema=ExistingUserSchema, status_code=201)
    def post(self):
        """Create a Single User"""

        user = UserService.create(request.parsed_obj)
        return user


@api.route("/<int:userId>")
@api.param("userId", "User database ID")
class UserIdResource(Resource):
    @responds(schema=ExistingUserSchema)
    def get(self, userId: int) -> User:
        """Get Single User"""

        return UserService.get_by_id(userId)

    def delete(self, userId: int) -> Response:
        """Delete Single User"""

        from flask import jsonify

        id = UserService.delete_by_id(userId)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=ExistingUserSchema, api=api)
    @responds(schema=ExistingUserSchema)
    def put(self, userId: int) -> User:
        """Update Single User"""

        changes = request.parsed_obj
        user = UserService.get_by_id(userId)
        return UserService.update(user, changes)