from pydantic import BaseModel

class accountsModel(BaseModel):
    id = int
    url = str
    account_name = str
    password =str

class organisationsModel(BaseModel):
    id = int
    name = str

class usersModel(BaseModel):
    id = int
    username = str
    first_name = str
    last_name = str
    password = str

