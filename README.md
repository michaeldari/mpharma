RESTful API that can allow us to utilize an internationally recognized set of diagnosis codes.

#Install Python, Pipenv and Postgres on your machine<br>
#Applicatin Setup Python (PipEnv) virtual environment<br>

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
python manage.py db migrate <br>
python manage.py db upgrade
</pre>

#run main API app<br>
<pre>
python run.py<br>
</pre>
