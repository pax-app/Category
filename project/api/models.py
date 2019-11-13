from database_singleton import Singleton
from flask import current_app
from flask_sqlalchemy import SQLAlchemy

db = Singleton().database_connection()


class Category():

    def to_json(self):
        pass


class Context():
    def __init__(self, category: Category):
        self._category = category

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category: Category):
        self._category = category

    def return_json(self, category):
        return self._category.to_json(category)


class GeneralCategory(db.Model, Category):

    __tablename__ = 'GENERAL_CATEGORY'

    general_category_id = db.Column(
        db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)

    def to_json(self, category):

        return {
            'id': category.general_category_id,
            'name': category.name,
        }


class ProviderCategory(db.Model, Category):
    __tablename__ = 'PROVIDER_CATEGORY'

    provider_category_id = db.Column(
        db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    general_category_id = db.Column(
        db.Integer, db.ForeignKey('general_category.id'))

    def to_json(self, category):

        return {
            'generalId': category.general_category_id,
            'id': category.provider_category_id,
            'name': category.name,
        }
