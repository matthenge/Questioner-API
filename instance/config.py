"""Configuration Module"""
import os


class Config(object):
    """Main configuration class"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = "andela"
    DBNAME = "dbname"
    DBUSER = "admin"
    DBHOST = "localhost"
    DBPASS = "andela"


class DevelopmentConfig(Config):
    """Development Configuration"""
    DEBUG = True
    DB_URL = "postgresql://admin:password@localhost/questioner"


class TestingConfig(Config):
    """Testing Configuration"""
    TESTING = True
    DEBUG = True
    DBNAME = "questioner_test"
    DBUSER = "admin"
    DBHOST = "localhost"
    DBPASS = "andela"
    TEST_DB_URL = "postgresql://admin:password@localhost/questioner_test"


class ProductionConfig(Config):
    """Production Configuration"""
    DEBUG = False
    TESTING = False
    DB_URL = os.getenv('DB_URL')


mainConfig = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}
