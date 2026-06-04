CREATE USER orozco_sacramentos_user WITH PASSWORD 'orozco_sacramentos_pass';
CREATE DATABASE orozco_sacramentos_db OWNER orozco_sacramentos_user;
GRANT ALL PRIVILEGES ON DATABASE orozco_sacramentos_db TO orozco_sacramentos_user;

uv add django djangorestframework djangorestframework-simplejwt  django-filter django-cors-headers psycopg2-binary python-decouple
