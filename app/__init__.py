from flask import Flask
from app.routes import shortener
from app.models import db
import config

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URL
    app.config['SECRET_KEY'] = config.SECRET_KEY

    db.init_app(app)
    app.register_blueprint(shortener)

    with app.app_context():
        db.create_all()

    return app
