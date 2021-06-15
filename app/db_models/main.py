import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref


Base = declarative_base()

from app.db_models.accounts import Accounts
from app.db_models.association_table import AssociationTable
from app.db_models.organisations import Organisations
from app.db_models.users import User
# We are using ORM from sqlalchemy so that we 
# can have a better representation of our relationships


# To avoid overwriting a database
if os.path.exists(str(os.getcwd())+'/x_system_db.db') == False:
    engine = create_engine('sqlite:///'+str(os.getcwd()) +'\database.db')
    Base.metadata.create_all(bind=engine)


# Connecting to an existing database

engine = create_engine('sqlite:///'+str(os.getcwd())+'/database.db', echo=False)


Session = sessionmaker(bind=engine)
session = Session()



