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

- Para hacer la creacion de las tablas, ejecute el modulo " app.py "

### Tests 

- Ejecute las pruebas unitarias, ejecute cada modulo o con el siguiente comando en la terminal:

tests>python -m unittest discover . -p test*.py

### Web service
- Es necesario instalar la libreria "Flask" para que el proyecto funcione, abra el simbolo de sistema y ejecute: pip install flask

- Ejecute el servidor web que esta el módulo "app.py", luego vaya a la dirección dada en la terminal y use la ruta que necesite (puede guiarse con las rutas de ejemplo en los comentarios del codigo)

### Web UI
- Instalar la libreria "flask" para que la Ui web funcione, abra el simbolo de sistema y ejecute: pip install flask

- Ejecutar el modulo view.py para la interfaz de usuario web, luego vaya a la direccion dada en la terminal y navegue entre las diferentes opciones 

Hecho por: Daniel Gomez Aristizabal
