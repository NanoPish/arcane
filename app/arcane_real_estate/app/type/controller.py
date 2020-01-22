from flask_restplus import Resource
from flask import request
from flask_restplus import Namespace
from flask_accepts import accepts, responds
from flask.wrappers import Response
from typing import List

from .schema import TypeSchema
from .model import Type
from .service import TypeService

api = Namespace("Type", description="Type information")


@api.route("/")
class TypeResource(Resource):
    """Types"""

    @responds(schema=TypeSchema, many=True)
    def get(self) -> List[Type]:
        """Get all Types"""

        return TypeService.get_all()

    @accepts(schema=TypeSchema, api=api)
    @responds(schema=TypeSchema)
    def post(self):
        """Create a Single Type"""

        return TypeService.create(request.parsed_obj)


@api.route("/<int:typeId>")
@api.param("typeId", "Type database ID")
class TypeIdResource(Resource):
    @responds(schema=TypeSchema)
    def get(self, typeId: int) -> Type:
        """Get Single Type"""

        return TypeService.get_by_id(typeId)

    def delete(self, typeId: int) -> Response:
        """Delete Single Type"""

        from flask import jsonify

        id = TypeService.delete_by_id(typeId)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=TypeSchema, api=api)
    @responds(schema=TypeSchema)
    def put(self, typeId: int) -> Type:
        """Update Single Type"""

        changes = request.parsed_obj
        type = TypeService.get_by_id(typeId)
        return TypeService.update(type, changes)