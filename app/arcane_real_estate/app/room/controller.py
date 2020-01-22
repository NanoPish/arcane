from flask_restplus import Resource
from flask import request
from flask_restplus import Namespace
from flask_accepts import accepts, responds
from flask.wrappers import Response
from typing import List

from .schema import RoomSchema
from .model import Room
from .service import RoomService

api = Namespace("Room", description="Room information")


@api.route("/")
class RoomResource(Resource):
    """Rooms"""

    @responds(schema=RoomSchema, many=True)
    def get(self) -> List[Room]:
        """Get all Rooms"""

        return RoomService.get_all()

    @accepts(schema=RoomSchema, api=api)
    @responds(schema=RoomSchema)
    def post(self):
        """Create a Single Room"""

        return RoomService.create(request.parsed_obj)


@api.route("/<int:roomId>")
@api.param("roomId", "Room database ID")
class RoomIdResource(Resource):
    @responds(schema=RoomSchema)
    def get(self, roomId: int) -> Room:
        """Get Single Room"""

        return RoomService.get_by_id(roomId)

    def delete(self, roomId: int) -> Response:
        """Delete Single Room"""

        from flask import jsonify

        id = RoomService.delete_by_id(roomId)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=RoomSchema, api=api)
    @responds(schema=RoomSchema)
    def put(self, roomId: int) -> Room:
        """Update Single Room"""

        changes = request.parsed_obj
        room = RoomService.get_by_id(roomId)
        return RoomService.update(room, changes)