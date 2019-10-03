import os
from flask import Flask
from project.api.views import provider_category_blueprint
from project.api.views import general_category_blueprint
from database import db, migrate


# instantiate the app
def create_app(script_info=None):
    # Instantiate the app
    app = Flask(__name__)

    # Set Configuration
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    db.init_app(app)
    migrate.init_app(app, db)

    # register blueprints
    app.register_blueprint(general_category_blueprint),
    app.register_blueprint(provider_category_blueprint),

    return app
