from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from . import Base



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(),primary_key = True) #db.column(type,primary key/foreign key etc)
    username = Column(String(40), unique=True)
    first_name = Column(String(50))
    last_name = Column(String(20))
    password = Column(String(20))


    #let's establish a one-to-many relationship: one user (parent) can have many friends (children)
    # Returns a list of rows from request model, that contains id of
    # current user in the for_id column.
    organisations = relationship("AssociationTable", backref = backref("users")) 
    '''creates a pseudo column called 'AssociationTable' in the users table'''