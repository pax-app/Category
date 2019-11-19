from flask_testing import TestCase
from project import create_app
from database_singleton import Singleton

app = create_app()
db = Singleton().database_connection()

class BaseTestCase(TestCase):
    
    def create_app(self):
        app.config.from_object('project.config.TestingConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()