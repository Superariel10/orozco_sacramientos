# orozco_sacramientos
#### Como instalar y ejecutar backend
#### 1. Clonar repositorio
#### https://github.com/Superariel10/orozco_sacramientos.git
#### 2. Entrar al proyecto
#### cd orozco/sacramientos
#### 3. Crear entorno virtual
#### python -m venv venv
#### 4. Activar el entorno
#### venv\Scripts\activate
#### 5. Instalar dependencias
#### pip install -r requirements.txt
#### 6. Migraciones
#### python manage.py migrate
#### 7. Ejecutar el servidor
#### python manage.py runserver
## Ejemplo de uso de la api
#### GET /api/registro_sacramento/
#### Autorization: Bearer eyJhbGciOiJIUzI1NiIs...
## Endpoints principales
## Sacramentos
#### GET /api/sacramentos/, POST  /api/sacramentos/, GET/api/sacramentos/id/, PUT/api/sacramentos/id, DELETE/api/sacramentos/id
## Registro de Sacramentos
#### GET /api/registro_sacramento/,POST /api/registro_sacramento/, GET /api/registro_sacramento/id/
#### Feligreses
#### GET     /api/feligreses/ , POST    /api/feligreses/
## Colleccion Postman
#### Revisar el codigo json para cargar las colecciones
