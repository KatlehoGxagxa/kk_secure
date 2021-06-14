from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from . import Base



class Accounts(Base):
    __tablename__ = 'accounts'
    url = Column(String(255)) #db.column(type,primary key/foreign key etc)
    account_name = Column(String(255))
    password = Column(String(225))



    friends = relationship("R", backref = backref(""))

