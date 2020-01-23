from flask_restplus import Resource
from flask import request
from flask_restplus import Namespace
from flask_accepts import accepts, responds
from flask.wrappers import Response
from typing import List
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.exceptions import NotFound
from .schema import PropertySchema
from .model import Property
from .service import PropertyService
from ..user.service import UserService

api = Namespace("Property", description="Property information")

@api.route("/")
class PropertyResource(Resource):
    """Properties"""

    @responds(schema=PropertySchema, many=True)
    @jwt_required
    def get(self) -> List[Property]:
        """Get all Properties"""

        return PropertyService.get_all()

    @accepts(schema=PropertySchema, api=api)
    @responds(schema=PropertySchema, status_code=201)
    @jwt_required
    def post(self):
        """Create a Single Property"""

        return PropertyService.create(request.parsed_obj, UserService.get_user_id_by_user_mail(get_jwt_identity()))


@api.route("/<int:propertyId>")
@api.param("propertyId", "Property database ID")
class PropertyIdResource(Resource):
    @responds(schema=PropertySchema)
    @jwt_required
    def get(self, propertyId: int) -> Property:
        """Get Single Property"""

        return PropertyService.get_by_id(propertyId)

    @jwt_required
    def delete(self, propertyId: int) -> Response:
        """Delete Single Property"""

        from flask import jsonify

        id = PropertyService.delete_by_id(propertyId, UserService.get_user_id_by_user_mail(get_jwt_identity()))
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=PropertySchema, api=api)
    @responds(schema=PropertySchema)
    @jwt_required
    def put(self, propertyId: int) -> Property:
        """Update Single Property"""

        changes = request.parsed_obj
        property = PropertyService.get_by_id(propertyId)

        if property is None:
            raise NotFound

        return PropertyService.update(property, changes, UserService.get_user_id_by_user_mail(get_jwt_identity()))
