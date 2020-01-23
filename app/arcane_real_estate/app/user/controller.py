from flask_restplus import Resource
from flask_restplus import Namespace
from flask_accepts import accepts, responds
from flask.wrappers import Response
from typing import List

from .schema import ExistingUserSchema, NewUserSchema, AuthUserSchema
from .model import User
from .service import UserService
from flask import jsonify, request

api = Namespace("User", description="User management")


@api.route("/auth")
class UserAuthResource(Resource):
    """User Auth"""

    @accepts(schema=AuthUserSchema, api=api)
    def post(self):
        """Authenticate a Single User"""

        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400

        mail = request.json.get('mail', None)
        password = request.json.get('password', None)
        if not mail:
            return jsonify({"msg": "Missing username parameter"}), 400
        if not password:
            return jsonify({"msg": "Missing password parameter"}), 400

        return UserService.authenticate(mail, password)


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
