from typing import List
from werkzeug.exceptions import Unauthorized
from app import db  # noqa
from .model import Room
from .interface import RoomInterface
from ..property.service import PropertyService

class RoomService:
    @staticmethod
    def get_all() -> List[Room]:
        return Room.query.all()

    @staticmethod
    def get_by_id(room_id: int) -> Room:
        return Room.query.get(room_id)

    @staticmethod
    def get_by_property_id(property_id: int) -> Room:
        return Room.query.filter(Room.property_id == property_id)

    @staticmethod
    def update(room: Room, room_change_updates: RoomInterface) -> Room:
        room.update(room_change_updates)
        db.session.commit()
        return room

    @staticmethod
    def delete_by_id(room_id: int) -> List[int]:
        room = Room.query.filter(Room.room_id == room_id).first()
        if not room:
            return []
        db.session.delete(room)
        db.session.commit()
        return [room_id]

    @staticmethod
    def create(new_attrs: RoomInterface, property_id: int, current_user_id) -> Room:
        if PropertyService.get_user_id_from_property_id(property_id) != current_user_id:
            raise Unauthorized

        new_room = Room(
            name=new_attrs["name"],
            description=new_attrs["description"],
            property_id=property_id,
        )

        db.session.add(new_room)
        db.session.commit()

        return new_room
