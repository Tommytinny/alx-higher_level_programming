#!/usr/bin/python3
""" List states """

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """ Class representing the state table """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        cascade="all,  delete-orphan",
        backref=backref("state", cascade="all"),
        single_parent=True)
