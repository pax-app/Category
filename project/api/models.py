from database import db
from flask import current_app


class GeneralCategory(db.Model):
    __tablename__ = 'GENERAL_CATEGORY'

    general_category_id = db.Column(
        db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)

    def __init__(self, name):
        self.name = name

    def to_json(self):
        return {
            'id': self.general_category_id,
            'name': self.name,
        }


class ProviderCategory(db.Model):
    __tablename__ = 'PROVIDER_CATEGORY'

    provider_category_id = db.Column(
        db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    general_category_id = db.Column(
        db.Integer, db.ForeignKey('general_category.id'))

    def __init__(self, name):
        self.name = name

    def to_json(self):
        return {
            'generalId': self.general_category_id,
            'id': self.provider_category_id,
            'name': self.name,
        }
