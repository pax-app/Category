from database import db
from project import create_app
from Flask import current_app


class General_Category(db.Model):
    __tablename__ = 'GENERAL_CATEGORY'


class Provider_Category(db.Model):
    __tablename__ = 'PROVIDER_CATEGORY'
