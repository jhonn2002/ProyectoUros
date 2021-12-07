from app import app
from flask import request, render_template,session
from sqlalchemy import exc 

from modelo.usuario import *
from modelo.formularioRol import *
from modelo.usuarioRol import *
from modelo.formularioRol import *

@app.route("/iniciarSesion", methods=['POST'])
def iniciarSesion():

    #Declaro 3 variables 
    tarea=False
    fr=[]
    ur=[]

    #Se guardan los valores que viene del formulario en las distintas varibles
    correo = request.form['txtUsuario']
    password=request.form['txtPassword']

    #Confirmo que las variables no esten vacias
    if(correo and password):
        try:
            #Consulta el usuario
            usuario = Usuario.query.filter(Usuario.usu_usuario==correo).filter(Usuario.usu_password==password).first()
            #Confirmo si el usuario no es null
            if(not usuario is None):
                #se crea la variable de sesión
                session['user']= usuario.usu_usuario 
                session['id']= usuario.id_usuario
                #Consulta si el usuario tiene rol
                ur = UsuarioRol.query.filter(UsuarioRol.usurol_id_usuario==usuario.id_usuario).all()
                #Confirmo si el UsuarioRol no es null
                if not ur is None:
                    for aur in ur:
                        fr = FormularioRol.query.filter(FormularioRol.forrol_id_rol==aur.usurol_id_rol).all()
                        if aur.usurol_id_rol == 1:
                            print("Entro 1")
                            return render_template("usuario/inicioAdmi.html", fr=fr, ur=ur)
                        elif aur.usurol_id_rol == 2:
                            print("Entro 2")
                            return render_template("usuario/inicio.html", fr=fr, ur=ur)
                            
                mensaje="No tiene asignado un rol por favor comunicarse con el servicio encargado 'Sistema'" 
                tarea=True 
            else:
                mensaje="Credenciales de ingreso no validas"   
                tarea=True        
        except exc.SQLAlchemyError as ex:
            mensaje = str(ex)           
    else:
        mensaje="Faltan datos"
    return render_template("frmCitaLogin.html",mensaje=mensaje, tarea=tarea)