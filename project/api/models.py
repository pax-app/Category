from database import db
from project import create_app
from Flask import current_app

class General_Category(db.Models):
    __tablename__ = 'GENERAL_CATEGORY'