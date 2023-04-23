#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Return the list of City instances with
            state_id equals to the current State.id
            """
            values_city = storage.all(City).values()
            list_city = []
            for city in values_city:
                if city.state_id == self.id:
                    list_city.append(city)
            return list_city

