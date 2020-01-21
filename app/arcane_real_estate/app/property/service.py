from typing import List

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
    def update(property: Property, property_change_updates: PropertyInterface) -> Property:
        property.update(property_change_updates)
        db.session.commit()
        return property

    @staticmethod
    def delete_by_id(property_id: int) -> List[int]:
        property = Property.query.filter(Property.property_id == property_id).first()
        if not property:
            return []
        db.session.delete(property)
        db.session.commit()
        return [property_id]

    @staticmethod
    def create(new_attrs: PropertyInterface) -> Property:
        new_property = Property(
            name=new_attrs["name"],
            description=new_attrs["description"],
            city=new_attrs["city"],
        )

        db.session.add(new_property)
        db.session.commit()

        return new_property
