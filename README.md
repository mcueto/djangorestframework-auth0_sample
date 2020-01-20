# djangorestframework-auth0_sample

Sample Django project for [djangorestframework-auth0](https://github.com/mcueto/djangorestframework-auth0) library usage.

<!-- Note: The curl command below will create a new ToDo ONLY if credentials are ok, otherwise you can only do a GET to that url. -->

🚀 Running the sample project
-----------
1. Clone this repository::
  ``` bash
  git clone https://github.com/mcueto/djangorestframework-auth0_sample.git
  ```

2. Go into the project folder::
  ``` bash
  cd djangorestframework-auth0_sample
  ```

3. Copy `.env.dist` to `.env` and set it's env vars content
  ``` bash
  cp .env.dist .env
  ```

4. Install requirements with pip:
  ``` bash
  pip install -r requirements.txt
  ```

5. Migrate:
  ``` bash
  python manage.py migrate
  ```

6. Run:
  ``` bash
  python manage.py runserver
  ```

7. Use:
  ``` bash
  curl -X POST -H 'Content-Type: application/json' -H 'Authorization:JWT  <your_access_token>' -d '{"text":"New todo"}' http://localhost:8000/api/todos/
  ```

Using RS256 keys
-----------
If you want to use an RS256 keypairs to verify your users, you must to do:
1. configure your Auth0 Client to use the RS256 algorithm
  ![alt text][img1]

2. Download your Client certificate (as a PEM file)
  ![alt text][img2]

3. Move your certificate to the *rsa_certificates* folder (only to keep things in order)

4. Append `cryptography` to `requirements.txt` and pip install it.

5. Add the following imports to your settings.py file
```
  from cryptography.x509 import load_pem_x509_certificate

  from cryptography.hazmat.backends import default_backend
```

6. Read your certificate before assing it to the settings
```
  certificate_text = open("rsa_certificates/certificate.pem", 'rb').read()
  certificate = load_pem_x509_certificate(certificate_text, default_backend())
  default_publickey = certificate.public_key()
```

7. Configure your certificate in your Django App
```
  AUTH0 = {
      'CLIENTS': {
          'web': {
              'AUTH0_CLIENT_ID': 'client_id',  #make sure it's the same string that aud attribute in your payload provides
              ...
              'AUTH0_ALGORITHM': 'RS256',
              'PUBLIC_KEY': default_publickey
          }
      },
      'JWT_AUTH_HEADER_PREFIX': 'JWT',  # default prefix used by djangorestframework_jwt
      'AUTHORIZATION_EXTENSION': False,  # default to False
  }
```
***You can view a full configuration file for RS256 in the RS256 branch***


  When you set **RS256** as the algorithm, both **AUTH_CLIENT_SECRET** and **CLIENT_SECRET_BASE64_ENCODED** settings are ignored.

  When you set **HS256** as the algorithm, the **PUBLIC_KEY** and **PRIVATE_KEY** settings of your Client are ignored.

[img1]: docs/images/rsa256-1.png "RS256 Selection"
[img2]: docs/images/rsa256-2.png "Certificate download"
