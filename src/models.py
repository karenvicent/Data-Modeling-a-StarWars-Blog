import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Character(Base):
    __tablename__ ='character'
    id = Column(Integer, primary_key=True)
    character_name = Column(String(200), nullable=False)
    gender = Column(String(50))
    hair_color = Column(String(50))
    eye_color = Column(String(50))
    skin_color = Column(String(50))
    url = Column(String(2000))

class Planet(Base):
    __tablename__ ='planets'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(200), nullable=False)
    population = Column(Integer)
    terrain = Column(String(50))
    climate = Column(String(50))
    url = Column(String(2000))

class User(Base):
    __tablename__ ='users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(200), nullable=False)
    mail = Column(String(200))
    password = Column(String(50))

class Favorite_Planets(Base):
    __tablename__ ='favorites_planets'
    id = Column(Integer, primary_key=True)
    id_planet = Column(Integer, ForeignKey('planets.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    
class Favorite_Characters(Base):
    __tablename__ ='favorites_characters'
    id = Column(Integer, primary_key=True)
    id_character = Column(Integer,  ForeignKey('character.id'))
    user_id = Column(Integer, ForeignKey('users.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')