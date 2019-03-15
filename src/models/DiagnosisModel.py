# src/models/DiagnosisModel.py
from . import db
import datetime
from marshmallow import fields, Schema


class DiagnosisModel(db.Model):
    # Diagnosis Model

    __tablename__ = 'diagnosis'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), nullable=False)
    description = db.Column(db.String, nullable=False)
    # icd_version = db.Column(db.String, db.ForeignKey('icd.version'), nullable=False)
    icd_version = db.Column(db.String, nullable=False)

    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def __init__(self, data):
        self.code = data.get('code').upper()
        self.description = data.get('description')
        self.icd_version = data.get('icd_version')
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
    def get_all_diagnosis(page):
        return DiagnosisModel.query.order_by(DiagnosisModel.code.asc()).paginate(page, 20, error_out=False).items

    @staticmethod
    def get_one_diagnosis(value):
        if value.isnumeric():
            return DiagnosisModel.query.filter_by(id=value).first()
        else:
            return DiagnosisModel.query.filter_by(code=value.upper()).first()

    def __repr__(self):
        return '<code {}>'.format(self.code)


class DiagnosisSchema(Schema):
    # Diagnosis Schema
    id = fields.Int(dump_only=True)
    code = fields.Str(required=True)
    icd_version = fields.Str(required=True)
    description = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
