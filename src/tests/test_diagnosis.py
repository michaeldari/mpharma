import unittest
import os
import json
import random
from ..app import create_app, db


class DiagnosisTest(unittest.TestCase):
    """
    Users Test Case
    """
    def setUp(self):
        """
        Test Setup
        """
        self.app = create_app("testing")
        self.client = self.app.test_client
        self.payload = {
            'code': 'A0103',
            'description':  'Typhoid fever with heart involvement',
            'icd_version':  'icd-10'
        }
        self.userPayload = {
            'name': 'michael',
            'email': 'm'+str(random.randint(1000, 100000))+'@mail.com',
            'password': 'passw0rd'
        }

        with self.app.app_context():
            # create all tables
            db.create_all()

    def test_diagnosis_creation(self):
        """ test diagnosis creation with valid credentials """
        res = self.client().post('/api/v1/users/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.userPayload))
        self.assertEqual(res.status_code, 201)
        api_token = json.loads(res.data).get('jwt_token')

        res = self.client().post('/api/v1/diagnosis/', headers={'Content-Type': 'application/json', 'api-token': api_token}, data=json.dumps(self.payload))
        json_data = json.loads(res.data)
        self.assertTrue(json_data.get('code'))
        self.assertTrue(json_data.get('description'))
        self.assertTrue(json_data.get('icd_version'))
        self.assertEqual(res.status_code, 201)

    def test_diagnosis_creation_with_existing_diagnosis_code(self):
        """ test diagnosis creation with already existing diagnosis code"""
        res = self.client().post('/api/v1/users/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.userPayload))
        self.assertEqual(res.status_code, 201)
        api_token = json.loads(res.data).get('jwt_token')

        res = self.client().post('/api/v1/diagnosis/', headers={'Content-Type': 'application/json', 'api-token': api_token}, data=json.dumps(self.payload))
        self.assertEqual(res.status_code, 201)
        res = self.client().post('/api/v1/diagnosis/', headers={'Content-Type': 'application/json', 'api-token': api_token}, data=json.dumps(self.payload))
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertTrue(json_data.get('error'))

    def test_user_creation_with_no_code(self):
        """ test diagnosis creation with no diagnosis code"""
        res = self.client().post('/api/v1/users/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.userPayload))
        self.assertEqual(res.status_code, 201)
        api_token = json.loads(res.data).get('jwt_token')

        diagnosis = {
            'description':  'Typhoid fever with heart involvement',
            'icd_version':  'icd-10'
        }
        res = self.client().post('/api/v1/diagnosis/', headers={'Content-Type': 'application/json', 'api-token': api_token}, data=json.dumps(diagnosis))
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertTrue(json_data.get('code'))

    def test_user_creation_with_no_description(self):
        """ test diagnosis creation with no email """
        res = self.client().post('/api/v1/users/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.userPayload))
        self.assertEqual(res.status_code, 201)
        api_token = json.loads(res.data).get('jwt_token')

        diagnosis = {
            'code': 'A0103',
            'icd_version':  'icd-10'
        }
        res = self.client().post('/api/v1/diagnosis/', headers={'Content-Type': 'application/json', 'api-token': api_token}, data=json.dumps(diagnosis))
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertTrue(json_data.get('description'))

    def test_user_creation_with_no_icd_version(self):
        """ test diagnosis creation with no email """
        res = self.client().post('/api/v1/users/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.userPayload))
        self.assertEqual(res.status_code, 201)
        api_token = json.loads(res.data).get('jwt_token')

        diagnosis = {
            'code': 'A0103',
            'description':  'Typhoid fever with heart involvement'
        }
        res = self.client().post('/api/v1/diagnosis/', headers={'Content-Type': 'application/json', 'api-token': api_token}, data=json.dumps(diagnosis))
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertTrue(json_data.get('icd_version'))

    def test_user_creation_with_empty_request(self):
        """ test diagnosis creation with empty request """
        res = self.client().post('/api/v1/users/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.userPayload))
        self.assertEqual(res.status_code, 201)
        api_token = json.loads(res.data).get('jwt_token')

        diagnosis = {}
        res = self.client().post('/api/v1/diagnosis/', headers={'Content-Type': 'application/json', 'api-token': api_token}, data=json.dumps(diagnosis))
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)

    def test_diagnosis_get_by_id(self):
        """ Test Diagnosis Get By ID """
        res = self.client().post('/api/v1/users/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.userPayload))
        self.assertEqual(res.status_code, 201)
        api_token = json.loads(res.data).get('jwt_token')

        payload = {
            'code': str(random.randint(1000, 100000)),
            'description':  'Typhoid fever with heart involvement',
            'icd_version':  'icd-10'
        }

        create_res = self.client().post('/api/v1/diagnosis/', headers={'Content-Type': 'application/json', 'api-token': api_token}, data=json.dumps(payload))
        self.assertEqual(create_res.status_code, 201)
        json_data = json.loads(create_res.data)

        res = self.client().get('/api/v1/diagnosis/'+str(json_data.get('code')), headers={'Content-Type': 'application/json', 'api-token': api_token})
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_diagnosis_get_all_by_pagination(self):
        """ Test Diagnosis Get All by pagination """
        res = self.client().post('/api/v1/users/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.userPayload))
        self.assertEqual(res.status_code, 201)
        api_token = json.loads(res.data).get('jwt_token')

        res = self.client().get('/api/v1/diagnosis/page/1', headers={'Content-Type': 'application/json', 'api-token': api_token})
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_diagnosis_delete_by_id(self):
        """ Test Diagnosis Delete By ID """
        res = self.client().post('/api/v1/users/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.userPayload))
        self.assertEqual(res.status_code, 201)
        api_token = json.loads(res.data).get('jwt_token')
        payload = {
            'code': str(random.randint(1000, 100000)),
            'description':  'Typhoid fever with heart involvement',
            'icd_version':  'icd-10'
        }
        create_res = self.client().post('/api/v1/diagnosis/', headers={'Content-Type': 'application/json', 'api-token': api_token}, data=json.dumps(payload))
        self.assertEqual(create_res.status_code, 201)
        json_data = json.loads(create_res.data)

        res = self.client().delete('/api/v1/diagnosis/'+str(json_data.get('id')), headers={'Content-Type': 'application/json', 'api-token': api_token})
        # json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 204)

    def test_user_update_diagnosis(self):
        """ Test User Update Me """
        res = self.client().post('/api/v1/users/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.userPayload))
        self.assertEqual(res.status_code, 201)
        api_token = json.loads(res.data).get('jwt_token')

        payload = {
            'code': str(random.randint(1000, 100000)),
            'description':  'Typhoid fever',
            'icd_version':  'icd-10'
        }
        res = self.client().post('/api/v1/diagnosis/', headers={'Content-Type': 'application/json', 'api-token': api_token}, data=json.dumps(payload))
        self.assertEqual(res.status_code, 201)
        json_data = json.loads(res.data)

        payload = {
            'code': str(random.randint(1000, 100000)),
            'description':  'Updated Typhoid fever',
            'icd_version':  'icd-10'
        }

        res = self.client().put('/api/v1/diagnosis/'+str(json_data.get('id')), headers={'Content-Type': 'application/json', 'api-token': api_token}, data=json.dumps(payload))
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json_data.get('description'), 'Updated Typhoid fever')

    def tearDown(self):
        """
        Tear Down
        """
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == "__main__":
    unittest.main()
