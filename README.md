RESTful API that can allow us to utilize an internationally recognized set of diagnosis codes.

#Install Python, Pipenv and Postgres on your machine<br>
#Applicatin Setup Python (PipEnv) virtual environment<br>

#move into project directory from GIT checkout and run the following commands from there

#start virtual environment<br>
<pre>pipenv shell</pre>

#install all dependencies<br>
<pre>pipenv install</pre>

#run the below to setup enviroment variable<br>
<pre>
export FLASK_ENV=development<br>
export JWT_SECRET_KEY=atUdEYVYP6RfCHz9zkADgS<br>
export DATABASE_URL=postgresql://DB_USERNAME:DB_PASSWORD@DB_HOST:DB_PORT/DB_NAME <br>
</pre> 
#run below to migrate the database<br>
<pre>
python manage.py db init<br>
python manage.py db migrate <br>
python manage.py db upgrade
</pre>

#run main API app<br>
<pre>
python run.py<br>
</pre>

#API REQUIREMENT
1. a Client accessing the diagnosis API should be first registered

<Pre>URL: http://127.0.0.1:5000/api/v1/users/</pre>
<Pre>REQUEST</pre>
<pre>{
	"email": "ansah@mail.com",
	"password": "password",
	"name": "ansah"
}</pre>

<Pre>RESPONSE</pre>
<pre>{
  "jwt_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTI3MjA1MDgsImlhdCI6MTU1MjYzNDEwOCwic3ViIjoxfQ.fhUexvS7J3Ns6wQpqdT89oK1jGbw9MzQO77_qUPtyVY"
}</pre>

2. the value of jwt_token from the user call is sent in the header of subsequent API resquest with key api-token

# SAMPLE Curl API CALLS


#Create a new API USER
<pre>curl --request POST \
  --url http://127.0.0.1:5000/api/v1/users/ \
  --header 'content-type: application/json' \
  --data '{
	"email": "michael@roninafrica.com",
	"password": "password",
	"name": "dari michael"
}'
</pre>
<pre>RESPONSE</pre>
<pre>
	{
  "jwt_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTI3MjA1MDgsImlhdCI6MTU1MjYzNDEwOCwic3ViIjoxfQ.fhUexvS7J3Ns6wQpqdT89oK1jGbw9MzQO77_qUPtyVY"
}
</pre>

<br><br><br>
#Login to get new token
<pre>
curl --request POST \
  --url http://127.0.0.1:5000/api/v1/users/login \
  --header 'content-type: application/json' \
  --data '{
	"email": "michael@roninafrica.com",
	"password": "password"
}'
</pre>
#Response
<pre>
	{
  "jwt_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTI3MjA1MDgsImlhdCI6MTU1MjYzNDEwOCwic3ViIjoxfQ.fhUexvS7J3Ns6wQpqdT89oK1jGbw9MzQO77_qUPtyVY"
}
</pre>

<br><br><br>
#Create new diagnosis
<pre>
curl --request POST \
  --url http://127.0.0.1:5000/api/v1/diagnosis/ \
  --header 'api-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTI3MjA1MDgsImlhdCI6MTU1MjYzNDEwOCwic3ViIjoxfQ.fhUexvS7J3Ns6wQpqdT89oK1jGbw9MzQO77_qUPtyVY' \
  --header 'content-type: application/json' \
  --data '{
	"code":"A010",
	"description":"Typhoid fever with heart involvement",
	"icd_version":"icd-10"
}'
</pre>
#Response
<pre>
{
  "code": "A010",
  "created_at": "2019-03-15T07:17:16.002415+00:00",
  "description": "Typhoid fever with heart involvement",
  "icd_version": "icd-10",
  "id": 11,
  "modified_at": "2019-03-15T07:17:16.002421+00:00"
}
</pre>

<br><br><br>
#Update diagnosis
<pre>
curl --request PUT \
  --url http://127.0.0.1:5000/api/v1/diagnosis/90 \
  --header 'api-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTI3MjA1MDgsImlhdCI6MTU1MjYzNDEwOCwic3ViIjoxfQ.fhUexvS7J3Ns6wQpqdT89oK1jGbw9MzQO77_qUPtyVY' \
  --header 'content-type: application/json' \
  --data '{
	"code":"A0102b",
	"description":"bbbTyphoid fever with heart involvement",
	"icd_version":"icd-10"
}'
</pre>
#Response
<pre>
{
  "code": "A010",
  "created_at": "2019-03-15T07:17:16.002415+00:00",
  "description": "Typhoid fever with heart involvement",
  "icd_version": "icd-10",
  "id": 11,
  "modified_at": "2019-03-15T07:17:16.002421+00:00"
}
</pre>


<br><br><br>
#Get all diagnosis by pagination diagnosis
<pre>
curl --request GET \
  --url http://127.0.0.1:5000/api/v1/diagnosis/page/1 \
  --header 'api-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTI3MjA1MDgsImlhdCI6MTU1MjYzNDEwOCwic3ViIjoxfQ.fhUexvS7J3Ns6wQpqdT89oK1jGbw9MzQO77_qUPtyVY'
</pre>
#Response
<pre>
[
  {
    "code": "A002",
    "created_at": "2019-03-15T07:16:34.122935+00:00",
    "description": "Typhoid fever with heart involvement",
    "icd_version": "icd-10",
    "id": 3,
    "modified_at": "2019-03-15T07:16:34.122939+00:00"
  },
  {
    "code": "A003",
    "created_at": "2019-03-15T07:16:38.573544+00:00",
    "description": "Typhoid fever with heart involvement",
    "icd_version": "icd-10",
    "id": 4,
    "modified_at": "2019-03-15T07:16:38.573548+00:00"
  },
  {
    "code": "A004",
    "created_at": "2019-03-15T07:16:42.927419+00:00",
    "description": "Typhoid fever with heart involvement",
    "icd_version": "icd-10",
    "id": 5,
    "modified_at": "2019-03-15T07:16:42.927423+00:00"
  }
  }
]
</pre>

<br><br><br>
#Get diagnosis record by record id or diagnosis code
<pre>
curl --request GET \
  --url http://127.0.0.1:5000/api/v1/diagnosis/3 \
  --header 'api-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTI3MjA1MDgsImlhdCI6MTU1MjYzNDEwOCwic3ViIjoxfQ.fhUexvS7J3Ns6wQpqdT89oK1jGbw9MzQO77_qUPtyVY'
</pre>
#Response
<pre>
{
  "code": "A002",
  "created_at": "2019-03-15T07:16:34.122935+00:00",
  "description": "Typhoid fever with heart involvement",
  "icd_version": "icd-10",
  "id": 3,
  "modified_at": "2019-03-15T07:16:34.122939+00:00"
}
</pre>

<br><br><br>
#Delete diagnosis record by record id or diagnosis code
<pre>
curl --request DELETE \
  --url http://127.0.0.1:5000/api/v1/diagnosis/2 \
  --header 'api-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTI3MjA1MDgsImlhdCI6MTU1MjYzNDEwOCwic3ViIjoxfQ.fhUexvS7J3Ns6wQpqdT89oK1jGbw9MzQO77_qUPtyVY'
</pre>

