from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from app.db_models.main import Base



class Organisations(Base):
    __tablename__ = 'organisations'
    id = Column(Integer(),primary_key = True) #db.column(type,primary key/foreign key etc)
    name = Column(String(40))
    accounts = relationship("Accounts", backref = backref("organisations"))
    users = relationship("User", backref = backref("organisations"))