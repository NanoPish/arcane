from flask_restplus import Resource
from flask import request
from flask_restplus import Namespace
from flask_accepts import accepts, responds
from flask.wrappers import Response
from werkzeug.exceptions import Unauthorized
from flask_jwt_extended import jwt_required, get_jwt_identity
from .schema import RoomSchema
from .model import Room
from .service import RoomService
from ..user.service import UserService
from ..property.service import PropertyService

api = Namespace("Room", description="Room information")


@api.route("/<int:roomId>")
@api.param("roomId", "Room unique ID")
class RoomIdResource(Resource):
    @responds(schema=RoomSchema)
    @jwt_required
    def get(self, roomId: int) -> Room:
        """Get Single Room"""

        return RoomService.get_by_id(roomId)

    def delete(self, roomId: int) -> Response:
        """Delete Single Room"""

        from flask import jsonify

        current_user_id = UserService.get_user_id_by_user_mail(get_jwt_identity())
        room: Room = RoomService.get_by_id(roomId)

        if PropertyService.get_user_id_from_property_id(roomId) != current_user_id:
            raise Unauthorized

        id = RoomService.delete_by_id(roomId)
        return jsonify(dict(status="Success", id=id))

    @accepts("ExistingRoom", schema=RoomSchema(exclude=["roomId", "propertyId"]), api=api)
    @responds(schema=RoomSchema)
    @jwt_required
    def put(self, roomId: int) -> Room:
        """Update Single Room"""

        changes = request.parsed_obj
        current_user_id = UserService.get_user_id_by_user_mail(get_jwt_identity())
        room: Room = RoomService.get_by_id(roomId)

        if PropertyService.get_user_id_from_property_id(roomId) != current_user_id:
            raise Unauthorized

        return RoomService.update(room, changes)
