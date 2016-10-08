# djangorestframework-auth0_sample

Simple Django Sample project to run DjangoRestFramework with Auth0.

Note: The curl command below will create a new ToDo ONLY if credentials are ok, otherwise you can only do a GET to that url.

How to run this
-----------
1. Clone this repository::
  >git clone https://github.com/mcueto/djangorestframework-auth0_sample.git

2. Go into the project folder::
  >cd djangorestframework-auth0_sample

3. Install requirements with pip:
  >pip install -r requirements.txt

4. Migrate:
  >python manage.py migrate

5. Run:
  >python manage.py runserver

6. Use:
  >curl -X POST -H 'Content-Type: application/json' -H 'Authorization:JWT  eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuaWNrbmFtZSI6ImV4YW1wbGUiLCJlbWFpbCI6ImV4YW1wbGVAbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6Ly9vdXJkb21haW4uZXUuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTIzNDU2Nzg5IiwiYXVkIjoiY2xpZW50X2lkIiwiZXhwIjoxNDgzMjI4Nzk5LCJpYXQiOjE0NzU2MjA2Njd9.frqteOpuH6Y3bu9fmbipXkW_YS_VUhwReecgYJoc0Ew' -d '{"text":"New todo"}' http://localhost:8000/api/todos/

Configure with your own credentials
-----------
Configure your settings.py AUTH0 configs in settings.py, remember that your aud attribute in the payload returned by Auth0 must be the same that client_id in settings.py and your client_secret must be the same that your Auth0 Client config.
