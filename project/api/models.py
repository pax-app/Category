from database import db
from flask import current_app

from flask_sqlalchemy import SQLAlchemy


class Category():

    def to_json(self):
        pass


class Context():
    """
    The Context defines the interface of interest to clients.
    """

    def __init__(self, category: Category):
        """
        Usually, the Context accepts a category through the constructor, but
        also provides a setter to change it at runtime.
        """

        self._category = category

    @property
    def category(self):
        """
        The Context maintains a reference to one of the Category objects. The
        Context does not know the concrete class of a category. It should work
        with all strategies via the Category interface.
        """

        return self._category

    @category.setter
    def category(self, category: Category):
        """
        Usually, the Context allows replacing a Category object at runtime.
        """

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
