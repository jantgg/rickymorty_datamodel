import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False, unique=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    active = Column(Boolean, default=True)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    char_id = Column(Integer, ForeignKey('character.id'))
    epi_id = Column(Integer, ForeignKey('episode.id'))
    loc_id = Column(Integer, ForeignKey('location.id'))

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    char_name = Column(String(250), nullable=False, unique=True)
    char_img = Column(String(250), nullable=False, unique=True)
    char_content = Column(String(250), nullable=False)

class Char_user(Base):
    __tablename__ = 'char_user'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    char_id = Column(Integer, ForeignKey('character.id'))
    char = relationship(Character)

class Episode(Base):
    __tablename__ = 'episode'
    id = Column(Integer, primary_key=True)
    epi_name = Column(String(250), nullable=False, unique=True)
    epi_img = Column(String(250), nullable=False, unique=True)
    epi_content = Column(String(250), nullable=False)


class Epi_user(Base):
    __tablename__ = 'epi_user'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    epi_id = Column(Integer, ForeignKey('episode.id'))
    epi = relationship(Episode)

class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    loc_name = Column(String(250), nullable=False, unique=True)
    loc_img = Column(String(250), nullable=False, unique=True)
    loc_content = Column(String(250), nullable=False)


class Loc_user(Base):
    __tablename__ = 'loc_user'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    loc_id = Column(Integer, ForeignKey('location.id'))
    loc = relationship(Location)





 
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
