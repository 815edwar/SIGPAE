# SIGPAE
PowerSoftProject

Para poder correr el proyecto es necesario contar con:
  
- SPRINT 1:
    - PDFMiner: 
        - Se puede descargar en https://pypi.python.org/pypi/pdfminer3k. 
        - Descomprimir el archivo descargado.
        - Moverse a la carpeta descomprimida en el terminal y ejecutar python setup.py
        El proyecto podrá ahora usar la herramienta PDFMiner.

- SPRINT 2:
    - XPDF:Se puede descargar escribiendo en el terminal:
        - sudo apt-get update  
        - sudo apt-get install xpdf
- SPRINT 3: 
	- pyocr, wand y PIL para python3; 
	- Librería psycop2 para python3
	- Para la conexión con SIGPAE es necesario crear una base de datos en postgreSQL. Para ello habra postgres en su consola y ejecute : create user sigpae with password '123123'; createdb sigaedb with owner sigpae. Finalmente ejecute los scripts SIGPAEsqchema.sql , SIGPAEdatos.sql , SIGPAEdatos2.sql que se encuetran en el repositorio.

        
- Además,podría ser necesario instalar dj-database-url :
- Escriba en el terminal: sudo pip3 install dj-database-url
