#!/usr/bin/python3

""" City Module for HBNB project """

import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        from models.place import Place

        __tablename__ = "cities"
        name = Column(String(128), nullable=False)

        state_id = Column(
                String(60),
                ForeignKey("states.id"),
                nullable=False)

        places = relationship(
                "Place",
                backref="cities",
                cascade="all, delete, delete-orphan")

    else:
        name = ""
        state_id = ""
