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
  >curl -X POST -H 'Content-Type: application/json' -H 'Authorization:JWT  eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuaWNrbmFtZSI6ImV4YW1wbGUiLCJlbWFpbCI6ImV4YW1wbGVAbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6Ly9vdXJkb21haW4uZXUuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTIzNDU2Nzg5IiwiYXVkIjoiY2xpZW50X2lkIiwiZXhwIjoxNTE0NzY0Nzk5LCJpYXQiOjE0NzU2MjA2NjcsImFwcF9tZXRhZGF0YSI6eyJhdXRob3JpemF0aW9uIjp7Imdyb3VwcyI6WyJhc2RzYWRkYXMiXX19fQ.WbwSQZZqhGPulJdJt1Ys43RAwfp_dGGljIrzHAew1lI' -d '{"text":"New todo"}' http://localhost:8000/api/todos/

Configure with your own credentials
-----------
Configure your settings.py AUTH0 configs in settings.py, remember that your aud attribute in the payload returned by Auth0 must be the same that client_id in settings.py and your client_secret must be the same that your Auth0 Client config.

Using RS256 keys
-----------
If you want to use an RS256 keypairs to verify your users, you must to do:
1. configure your Auth0 Client to use the RS256 algorithm
  ![alt text][img1]

2. Download your Client private key(certificate as a PEM file)
  ![alt text][img2]

3. Generate your Client public key
  >openssl rsa -in <YOUR_CERTIFICATE.pem> -pubout -outform PEM -out <YOUR_CERTIFICATE>.pem.pub

4. Move your public and private keys to the *rsa_certificates* folder (only to keep things in order)

5. Configure your Client public and private keys in your Django App
```
  AUTH0 = {
      'CLIENTS': {
          'web': {
              'AUTH0_CLIENT_ID': 'client_id',  #make sure it's the same string that aud attribute in your payload provides
              ...
              'AUTH0_ALGORITHM': 'RS256',
              'PUBLIC_KEY': open("rsa_certificates/<YOUR_CERTIFICATE>.pem.pub").read(),  # used only for RS256
              'PRIVATE_KEY': open("rsa_certificates/<YOUR_CERTIFICATE>.pem").read()  # used only for RS256
          }
      },
      'JWT_AUTH_HEADER_PREFIX': 'JWT',  # default prefix used by djangorestframework_jwt
      'AUTHORIZATION_EXTENSION': False,  # default to False
  }
```

  When you set **RS256** as the algorithm, both **AUTH_CLIENT_SECRET** and **CLIENT_SECRET_BASE64_ENCODED** settings are ignored.

  When you set **HS256** as the algorithm, the **PUBLIC_KEY** and **PRIVATE_KEY** settings of your Client are ignored.

[img1]: docs/images/rsa256-1.png "RS256 Selection"
[img2]: docs/images/rsa256-2.png "Certificate download"
