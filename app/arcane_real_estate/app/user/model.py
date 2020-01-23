from sqlalchemy import Integer, Column, String, DateTime
from sqlalchemy.orm import relationship
from app import db  # noqa
from .interface import UserInterface


class User(db.Model):
    """A Arcanific User"""

    __tablename__ = "user"
    user_id = Column(Integer(), primary_key=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    birth_date = Column(DateTime, nullable=False)

    properties = relationship("Property", back_populates="user")

    def update(self, changes):
        for key, val in changes.items():
            setattr(self, key, val)
        return