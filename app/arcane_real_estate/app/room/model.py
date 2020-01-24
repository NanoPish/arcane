from sqlalchemy import Integer, Column, String, ForeignKey
from .. import db  # noqa
from .interface import RoomInterface


class Room(db.Model):
    """A Arcanific Room"""

    __tablename__ = "room"
    room_id = Column(Integer(), primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    property_id = Column(Integer, ForeignKey('property.property_id'), nullable=False)

    def update(self, changes):
        for key, val in changes.items():
            if key not in ["room_id", "property_id"]:
                setattr(self, key, val)
        return
