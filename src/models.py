import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

class Types(enum.Enum):
    IMAGE = 'image'
    VIDEO = 'video'

class User(Base):
    __tablename__='user'
    email = Column(String, primary_key=True)
    user_name = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    phone = Column(Integer, nullable=True)
    web = Column(String(50), nullable=True)
    password = Column(String(50), nullable=False)
    follower = relationship('follower')
    following = relationship('following')
    post = relationship('post')
    comment = relationship('comment')

class Follower(Base):
    __tablename__='follower'
    id = Column(String, primary_key=True)
    user_name = Column(String(50), nullable=False)
    user_id = Column(String(50), ForeignKey('user.user_name'))

class Following(Base):
    __tablename__='following'
    id = Column(String, primary_key=True)
    user_name = Column(String(50), nullable=False)
    user_id = Column(String(50), ForeignKey('user.user_name'))
    
class Post(Base):
    __tablename__='post'
    id = Column(String, primary_key=True)
    user_id = Column(String(50), ForeignKey('user.user_name'))
    post_text = Column(String(300), nullable=True)
    media = relationship('media')
    comment = relationship('comment')
    
    
class Media(Base):
    __tablename__='Media'
    id = Column(String, primary_key=True)
    post_id = Column(String(50), ForeignKey('post.id'))
    type = Column(Enum(Types), nullable=False)
    url = Column(String(50), nullable=False)
    
class Comment(Base):
    __tablename__='comment'
    id = Column(String, primary_key=True)
    post_id = Column(String(50), ForeignKey('post.id'))
    comment_text = Column(String(300), nullable=False)
    user_id = Column(String(50), ForeignKey('user.user_name'))
    
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
