from typing import List
from .. import db  # noqa
from .model import Type
from .interface import TypeInterface


class TypeService:
    @staticmethod
    def get_all() -> List[Type]:
        return Type.query.all()

    @staticmethod
    def get_by_id(type_id: int) -> Type:
        return Type.query.get(type_id)

    @staticmethod
    def update(type: Type, type_change_updates: TypeInterface) -> Type:
        type.update(type_change_updates)
        db.session.commit()
        return type

    @staticmethod
    def delete_by_id(type_id: int) -> List[int]:
        type = Type.query.filter(Type.type_id == type_id).first()
        if not type:
            return []
        db.session.delete(type)
        db.session.commit()
        return [type_id]

    @staticmethod
    def create(new_attrs: TypeInterface) -> Type:
        new_type = Type(
            type_id=new_attrs["type_id"],
            name=new_attrs["name"],
            description=new_attrs["description"],
        )

        db.session.add(new_type)
        db.session.commit()

        return new_type
