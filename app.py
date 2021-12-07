import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Crear un objeto de tipo Flask
app = Flask(__name__)
app.secret_key = os.urandom(32) #es neceario para poder crear variables de sesión

#cadena de conexión a la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Jhonn2002*@localhost/urosoft'

db = SQLAlchemy(app)

#configurar carpeta donde se van a subir las fotos
app.config['UPLOAD_FOLDER'] = 'static/documentosSolicitud'


from controlador.inicioController import *
from controlador.usuarioController import *

from controlador.formularioController import *
from controlador.formularioRolController import *
from controlador.personaController import *
from controlador.rolController import *
from controlador.usuarioRolController import *

# from modelo.persona import Persona
# from modelo.rol import Rol
# from modelo.formulario import Formulario
# from modelo.usuario import Usuario
# from modelo.usuarioRol import UsuarioRol
# from modelo.formularioRol import FormularioRol

# db.create_all()
# db.session.commit()

if __name__ == '__main__':
    app.run(port=5000, debug=True)
    