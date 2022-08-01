import datetime

import sqlalchemy.orm

from base import Base


class User(Base):
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    surname = sqlalchemy.Column(sqlalchemy.String)
    login = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=False)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    create_ts = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.utcnow())

    def __repr__(self) -> str:
        return f"User id={self.id}, name={self.name}, surname={self.surname}"


class Party(Base):
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    create_ts = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.utcnow())

    def __repr__(self) -> str:
        return f"Party id={self.id}"


class PartyUsers(Base):
    id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("party.id"))
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("user.id"))
    music_json = sqlalchemy.Column(sqlalchemy.JSON)

    user: User = sqlalchemy.orm.relationship('User', foreign_keys="User.id")
    party: Party = sqlalchemy.orm.relationship('Party', foreign_keys="Party.id")

    def __repr__(self) -> str:
        return f"Party id={self.id}, user_id={self.user_id}"
