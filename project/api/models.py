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
            'general_category.id': self.general_category_id,
            'general_category.name': self.name,
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
            'provider_category.id': self.provider_category_id,
            'provider_category.name': self.name,
        }


class Works(db.Model):
    __tablename__ = 'works'

    provider_category_id = db.Column(
        db.Integer, db.ForeignKey('PROVIDER_CATEGORY.id'), primary_key=True)
    provider_id = db.Column(db.Integer, primary_key=True, nullable=False)
