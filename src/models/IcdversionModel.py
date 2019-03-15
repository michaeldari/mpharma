# src/models/IcdversionModel.py
from marshmallow import fields, Schema
import datetime
from . import db
from .DiagnosisModel import DiagnosisSchema


class IcdversionModel(db.Model):
    # Icdversion Model

    # table name
    __tablename__ = 'icd'

    version = db.Column(db.String(10), primary_key=True, nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    # diagnosis = db.relationship('DiagnosisModel', backref='icd', lazy=True)

    # class constructor
    def __init__(self, data):
        # Class constructor

        self.version = data.get('version')
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_version():
        return IcdversionModel.query.all()

    @staticmethod
    def get_one_version(version):
        return IcdversionModel.query.get(version)

    def __repr(self):
        return '<version {}>'.format(self.version)


class IcdversionSchema(Schema):
    version = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
    # diagnosis = fields.Nested(DiagnosisSchema, many=True)

