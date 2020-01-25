class Config(object):
    PORT = 8080
    HOST = "0.0.0.0"
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(Config):
    pass


class Testing(Config):
    pass


class Production(Config):
    pass


