from app.db_models.organisations import Organisations
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from app.db_models.main import Base



class Accounts(Base):
    __tablename__ = 'accounts'

    id = Column(Integer(),primary_key = True)
    url = Column(String(255)) #db.column(type,primary key/foreign key etc)
    account_name = Column(String(255))
    password = Column(String(225))
    Organisations = relationship("Organisations", backref = backref("accounts"))

