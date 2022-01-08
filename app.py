from flask import Flask

# Crear un objeto de tipo Flask
app = Flask(__name__)

#configurar carpeta donde se van a subir las fotos
app.config['UPLOAD_FOLDER'] = 'static/archivos'

from controlador.inicioController import *
from controlador.usuarioController import *

if __name__ == '__main__':
    app.run(port=5000, debug=True)
    