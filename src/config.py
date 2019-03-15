# /src/config.py

# import os
# from dotenv import load_dotenv, find_dotenv

# load_dotenv(find_dotenv())


class Development(object):
    # Development environment configuration
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "atUdEYVYP6RfCHz9zkADgS"
    SQLALCHEMY_DATABASE_URI = "postgresql://michael:Ronin@247@localhost:5432/mpharma"


class Production(object):
    # Production environment configurations
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "atUdEYVYP6RfCHz9zkADgS"
    JWT_SECRET_KEY = "postgresql://michael:Ronin@247@localhost:5432/mpharma"


class Testing(object):
    # Development environment configuration
    TESTING = True
    JWT_SECRET_KEY = "atUdEYVYP6RfCHz9zkADgS"
    SQLALCHEMY_DATABASE_URI = "postgresql://michael:Ronin@247@localhost:5432/mpharma"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app_config = {
    'development': Development,
    'production': Production,
    'testing': Testing
}
