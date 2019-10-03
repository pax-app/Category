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
