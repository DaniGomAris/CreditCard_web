Credit card web

Recomendaciones: Abra este proyecto en Pycharm

---- Configuracion de la base de datos ----

Es necesario instalar la libreria "PsycoPG2" para que el proyecto funcione, abra el simbolo de sistema y ejecute: pip install psycopg2

Abra SecretConfig_example.py, sigue las instrucciones para inicializar el proyecto con tu base de datos

La carpeta "Controllers" contiene los modulos que realizaran las operaciones de creacion en la base de datos

Para hacer la creacion de las tablas, ejecuta la funcion de "create_table()" en "ControllerCreditCard" y "ControllerPaymentPlan"

---- Tests ----

Ejecute las pruebas unitarias con el siguiente comando en la terminal:

tests>python -m unittest discover . -p test*.py

---- Web ----
Es necesario instalar la libreria "Flask" para que el proyecto funcione, abra el simbolo de sistema y ejecute: pip install flask

Ejecute el servidor web que esta el módulo "app.py", luego vaya a la dirección dada en la terminal y use la ruta que necesite (puede guiarse con las rutas de ejemplo en los comentarios del codigo)

Autor: Daniel Gomez Aristizabal