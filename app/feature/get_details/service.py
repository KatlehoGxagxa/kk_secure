from app.db_models.models import userModel
from sqlalchemy.orm import session
from app.db_models import Session
from app.db_models.users import User
import math

class get_details():
    
    def __init__(self, inputs: userModel):
        self.__inputs = inputs
        self.session = Session()


