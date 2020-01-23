from typing import List
from werkzeug.exceptions import Unauthorized
from app import db  # noqa
from .model import Property
from .interface import PropertyInterface


class PropertyService:
    @staticmethod
    def get_all() -> List[Property]:
        return Property.query.all()

    @staticmethod
    def get_by_id(property_id: int) -> Property:
        return Property.query.get(property_id)

    @staticmethod
    def update(property_to_update: Property,
               property_change_updates: PropertyInterface,
               user_id: int) -> Property:

        if property_to_update.user_id != user_id:
            raise Unauthorized

        property_to_update.update(property_change_updates)
        db.session.commit()

        return property_to_update

    @staticmethod
    def delete_by_id(property_id: int, user_id: int) -> List[int]:
        property = Property.query.filter(Property.property_id == property_id).first()

        if not property:
            return []
        if property.user_id != user_id:
            raise Unauthorized

        db.session.delete(property)
        db.session.commit()

        return [property_id]

    @staticmethod
    def create(new_attrs: PropertyInterface, user_id: int) -> Property:
        new_property = Property(
            name=new_attrs["name"],
            description=new_attrs["description"],
            city=new_attrs["city"],
            type_id=new_attrs["type_id"],
            user_id=user_id,
        )

        db.session.add(new_property)
        db.session.commit()

        return new_property
