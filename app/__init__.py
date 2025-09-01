# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    db_path = os.path.join(app.instance_path, "unisafe.db")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    os.makedirs(app.instance_path, exist_ok=True)
    db.init_app(app)

    @app.get("/")
    def index():
        return {"message": " API running"}

    # 🔑 Registrer API-blueprintet
    from .api import api
    app.register_blueprint(api, url_prefix="/api")

    # (valgfritt) skriv ut rute-kart for feilsøking
    with app.app_context():
        print("Routes:", [str(r) for r in app.url_map.iter_rules()])

    return app



