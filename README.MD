# Credit card web

## Instrucciones en Español
Recomendaciones: Abra este proyecto en Pycharm

### Configuracion de la base de datos

- Crear una cuenta en la pagina de base de datos de su preferencia

- Crear una base de datos

- Obtener los detalles de conexion en el dasboard en su base de datos Get the connection details in the dashboard of your database on neondb

- Instalar la libreria "PsycoPG2" para que el proyecto funcione, abra el simbolo de sistema y ejecute: pip install psycopg2

- Abra SecretConfig-sample.py, sigue las instrucciones para inicializar el proyecto con tu base de datos

- La carpeta "Controllers" contiene los modulos que realizaran las operaciones de creacion en la base de datos

- Para hacer la creacion de las tablas, ejecute el modulo " app.py " o ejecute en los controladores los metodos "create_table()"

### Tests 

- Para ejecutar las pruebas unitarias, ejecute cada modulo o con el siguiente comando en la terminal:

tests>python -m unittest discover . -p test*.py

### Servicio Web

- Es necesario instalar la libreria "Flask" para que el proyecto funcione, abra el simbolo de sistema y ejecute: pip install flask

- Ejecute el servidor web que esta el módulo "app.py", luego vaya a la dirección dada en la terminal y use la ruta que necesite (puede guiarse con las rutas de ejemplo en los comentarios del codigo)

### Web UI
- Instalar la libreria "flask" para que la Ui web funcione, abra el simbolo de sistema y ejecute: pip install flask

- Ejecutar el modulo view.py para la interfaz de usuario web, luego vaya a la direccion dada en la terminal y navegue entre las diferentes opciones 

Hecho por: Daniel Gomez Aristizabal

----

## English instructions
Recomendations: Abra este proyecto en Pycharm

### Database configuration

- Create an account on the database server of your choice

- Create a database

- Get the connection details in the dashboard of your database

- Install the library " PsycoPG2 " for the project to work, open the command prompt and run: pip install psycopg2

- Abra " SecretConfig-sample.py ", sigue las instrucciones para inicializar el proyecto con tu base de datos

- The folder: "Controllers", contains the modules that perform the creation operations on the database

- To create the tables, run the module: "app.py" or run the methods: "create_table()" in the controllers.

### Tests 

- To run the unit tests, run each module or with the following command in the terminal:

tests>python -m unittest discover . -p test*.py

### Web service
- It is necessary to install the "Flask" library for the project to work, open the command prompt and run: pip install flask

- Run the web server that is the "app.py" module, then go to the address given in the terminal and use the path you need (you can guide yourself with the example paths in the code comments)

### Web UI
- Install the "flask" library so that the web UI works, open the command prompt and run: pip install flask

- Run the view.py module for the web UI, then go to the address given in the terminal and navigate between the different options

By: Daniel Gomez Aristizabal
