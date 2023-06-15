#!/usr/bin/python3
""" State Module for HBNB project """

import os
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        from models.city import City

        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship(
                "City",
                backref="state",
                cascade="all, delete")
    else:
        name = ""

        @property
        def cities(self):
            """ returns all cities with state_id == State.id """

            from models import storage

            list_cities = []
            for key, obj in storage.all().items():
                if "City" in key:
                    if obj.state_id == self.id:
                        list_cities.append(obj)

            return list_cities
