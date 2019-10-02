from database import db
from Flask import current_app
from project import create_app


class GeneralCategory(db.Model):
    __tablename__ = 'GENERAL_CATEGORY'

    general_category_id = db.Column(
        db.Integer, primary_key=True, autoincrement=True)
    general_category_name = db.Column(db.String(50), nullable=False)

    def __init__(self, name):
        self.general_category_name = name

    def to_json(self):
        return {
            'general_category_id': self.general_category_id,
            'general_category_name': self.name,
        }


class ProviderCategory(db.Model):
    __tablename__ = 'PROVIDER_CATEGORY'

    provider_category_id = db.Column(
        db.Integer, primary_key=True, autoincrement=True)
    provider_category_name = db.Column(db.String(50), nullable=False)
    general_category_id = db.Column(
        db.Integer, db.ForeignKey('general_category.id'))

    def __init__(self, name):
        self.provider_category_name = name

    def to_json(self):
        return {
            'provider_category_id': self.provider_category_id,
            'provider_category_name': self.name,
        }
