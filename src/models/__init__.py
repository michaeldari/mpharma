# src/models/__init__.py

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# initialize our db
db = SQLAlchemy()
bcrypt = Bcrypt()


from .UserModel import UserModel, UserSchema
from .IcdversionModel import IcdversionModel, IcdversionSchema
from .DiagnosisModel import DiagnosisModel, DiagnosisSchema