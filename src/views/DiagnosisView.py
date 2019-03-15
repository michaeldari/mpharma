# /src/views/DiagnosisView.py
from flask import request, g, Blueprint, json, Response
from ..shared.Authentication import Auth
from ..models.DiagnosisModel import DiagnosisModel, DiagnosisSchema

diagnosis_api = Blueprint('diagnosis_api', __name__)
diagnosis_schema = DiagnosisSchema()


@diagnosis_api.route('/', methods=['POST'])
@Auth.auth_required
def create():
    # Create Diagnosis Function

    req_data = request.get_json()
    data, error = diagnosis_schema.load(req_data)
    if error:
        return custom_response(error, 400)

    # check if diagnosis code already exist in the db
    diagnosis_in_db = DiagnosisModel.get_one_diagnosis(data.get('code'))
    if diagnosis_in_db:
        message = {'error': 'Diagnosis record with given code already exist, please supply another code'}
        return custom_response(message, 400)

    diagnosis = DiagnosisModel(data)
    diagnosis.save()
    data = diagnosis_schema.dump(diagnosis).data
    return custom_response(data, 201)


@diagnosis_api.route('/page/<int:page>', methods=['GET'])
def get_all(page):
    """
    Get All Diagnosis
    """
    diagnosis = DiagnosisModel.get_all_diagnosis(page)
    data = diagnosis_schema.dump(diagnosis, many=True).data
    return custom_response(data, 200)


@diagnosis_api.route('/<string:code>', methods=['GET'])
def get_one(code):
    """
    Get A Diagnosis
    """
    diagnosis = DiagnosisModel.get_one_diagnosis(code)
    if not diagnosis:
        return custom_response({'error': 'diagnosis not found'}, 404)
    data = diagnosis_schema.dump(diagnosis).data
    return custom_response(data, 200)


@diagnosis_api.route('/<string:code>', methods=['PUT'])
@Auth.auth_required
def update(code):
    """
    Update A Diagnosis
    """
    req_data = request.get_json()
    diagnosis = DiagnosisModel.get_one_diagnosis(code)
    if not diagnosis:
        return custom_response({'error': 'diagnosis not found'}, 404)

    data, error = diagnosis_schema.load(req_data, partial=True)
    if error:
        return custom_response(error, 400)
    diagnosis.update(data)

    data = diagnosis_schema.dump(diagnosis).data
    return custom_response(data, 200)


@diagnosis_api.route('/<string:code>', methods=['DELETE'])
@Auth.auth_required
def delete(code):
    """
    Delete A Diagnosis
    """
    diagnosis = DiagnosisModel.get_one_diagnosis(code)
    if not diagnosis:
        return custom_response({'error': 'diagnosis not found'}, 404)

    diagnosis.delete()
    return custom_response({'message': 'deleted'}, 204)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )

