from flask import Flask
from .config import Config
from .extensions import db, jwt
from .routes import register_routes
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)  
    jwt.init_app(app)

    with app.app_context():
        db.create_all()

    register_routes(app)

    return app