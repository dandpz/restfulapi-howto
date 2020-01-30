import os


class Config(object):
    PORT = 8080
    HOST = "0.0.0.0"
    DEBUG = True

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/test.db"
    FLASK_ENV = "development"


class Testing(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/test.db"
    FLASK_ENV = "development"


class Production(Config):
    PORT = os.getenv("PORT")
    HOST = os.getenv("HOST")
    DEBUG = False
    TESTING = False
    FLASK_DEBUG = False
    FLASK_ENV = "production"

    SQLALCHEMY_DATABASE_URI = os.getenv("DB_URI")
