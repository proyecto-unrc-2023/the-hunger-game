import os


class Config(object):
    TESTING = False

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JWT_SECRET_KEY = "clave_secreta"
    SQLALCHEMY_DATABASE_URI = "sqlite:///db_user.db"


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
