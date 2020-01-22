from sqlalchemy import Integer, Column, String
from app import db  # noqa
from .interface import RoomInterface


class Room(db.Model):
    """A Flaskerific Room"""

    __tablename__ = "room"
    room_id = Column(Integer(), primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)

    def update(self, changes):
        for key, val in changes.items():
            setattr(self, key, val)
        return