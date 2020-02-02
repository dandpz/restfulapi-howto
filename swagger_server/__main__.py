#!/usr/bin/env python3

import connexion
from flask import Flask
from swagger_ui_bundle import swagger_ui_3_path
import os
from swagger_server.database import db


from swagger_server import encoder

options = {"swagger_path": swagger_ui_3_path}


def create_app():
    _app = connexion.App(__name__, specification_dir="./swagger/")
    _app.app.json_encoder = encoder.JSONEncoder
    _app.add_api(
        "swagger.yaml", arguments={"title": "TO-DO list"}, options=options,
    )
    configure_app(_app.app)
    init_app(_app.app)
    return _app


def configure_app(flask_app):
    flask_app.config.from_object(
        f"swagger_server.config.{os.getenv('APPLICATION_ENV', 'Development')}"
    )

    @flask_app.before_first_request
    def create_database():
        db.drop_all()
        db.create_all()


def init_app(flask_app: Flask):
    db.init_app(flask_app)


if __name__ == "__main__":
    app = create_app()
    app.run(port=app.app.config["PORT"])
