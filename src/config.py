class BaseConfig:
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = ''

class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'DATABASE_TEST_URL'

class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'DATABASE_URL'