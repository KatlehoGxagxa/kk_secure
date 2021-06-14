from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from datetime import datetime
from . import Base


class AssociationTable(Base):
    __tablename__ = 'association_table'

    user_id= Column(Integer(), ForeignKey("organisations.id"), primary_key = True) #id of user requesting
    organisation_id = Column(Integer(), ForeignKey("users.id"), primary_key = True ) #id of user being requested
    is_admin = Column(Integer(), default=0) 


