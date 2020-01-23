from sqlalchemy import Integer, Column, String, Date
from sqlalchemy.orm import relationship
from app import db  # noqa
from .interface import UserInterface
from passlib.apps import custom_app_context as pwd_context

class User(db.Model):
    """A Arcanific User"""

    __tablename__ = "user"
    user_id = Column(Integer(), primary_key=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    birth_date = Column(Date, nullable=False)
    mail = db.Column(db.String(64), index=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)


    properties = relationship("Property", back_populates="user")

    def update(self, changes):
        for key, val in changes.items():
            setattr(self, key, val)
        return

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)