from app import app
from flask import render_template, session, request

from modelo.usuarioRol import *
from modelo.formularioRol import *

#Rutas de paginas principal
@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/citaLogin')
def citaLogin():
    return render_template('frmCitaLogin.html')

@app.route('/nuestraClinica')
def nuestraClinica():
    return render_template('nuestraClinica.html')

@app.route('/derechosDeberes')
def derechosDeberes():
    return render_template('derechosDeberes.html')

@app.route('/portafolio')
def portafolio():
    return render_template('portafolio.html')

@app.route('/proyectos')
def proyectos():
    return render_template('proyecto.html')

@app.route('/proyectoAngel')
def proyectoAngel():
    return render_template('proyectoAngel.html')

@app.route('/chequeoEjecutivo')
def chequeoEjecutivo():
    return render_template('chequeoEjecutivo.html')

@app.route('/trabajeConNosotros')
def trabajeConNosotros():
    return render_template('trabajeConNosotros.html')

@app.route('/planCanguro')
def planCanguro():
    return render_template('planCanguro.html')

@app.route('/galeriaFotos')
def galeriaFotos():
    return render_template('galeria.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/formPqr')
def formPqr():
    return render_template('formularioPqr.html')

@app.route('/salaCirugia')
def salaCirugia():
    return render_template('salaCirugia.html')

@app.route('/hospitalizacionGeneral')
def hospitalizacionGeneral():
    return render_template('hospitalizacionGeneral.html')

@app.route('/neuroCirugia')
def neuroCirugia():
    return render_template('neuroCirugia.html')

@app.route('/urgencia')
def urgencia():
    return render_template('urgencia.html')

@app.route('/hemodinamia')
def hemodinamia():
    return render_template('hemodinamia.html')

@app.route('/ginecologia')
def ginecologia():
    return render_template('ginecologia.html')

@app.route('/cardiologia')
def cardiologia():
    return render_template('cardiologia.html')

@app.route('/gastroenterologia')
def gastroenterologia():
    return render_template('gastroenterologia.html')

@app.route('/hospiCasa')
def hospiCasa():
    return render_template('hospiCasa.html')

@app.route('/consultaExterna')
def consultaExterna():
    return render_template('consultaExterna.html')

@app.route('/cardiovascular')
def cardiovascular():
    return render_template('cardiovascular.html')

@app.route('/imagenologia')
def imagenologia():
    return render_template('imagenologia.html')

@app.route('/laboratorio')
def laboratorio():
    return render_template('laboratorio.html')

#Rutas del usuario

@app.route("/inicioUsuario")
def inicioUsuario():
    tarea=False
    fr=[]
    ur=[]
    if("user" in session and "id" in session):
        ur = UsuarioRol.query.filter(UsuarioRol.usurol_id_usuario==session["id"]).all()
        if not ur is None:
            for aur in ur:
                if aur.usurol_id_rol == 2:
                    fr = FormularioRol.query.filter(FormularioRol.forrol_id_rol==2).all()
                    return render_template("usuario/inicio.html", fr=fr, ur=ur)
                else:
                    mensaje="Error de permisos" 
                    tarea=True
        else:
            mensaje="No tiene asignado un rol por favor comunicarse con el servicio encargado 'Sistema'" 
            tarea=True 
    else:
        tarea=True
        mensaje="Debe primero iniciar Sesion"
    return render_template("frmCitaLogin.html",mensaje=mensaje, tarea=tarea)


#Rutas del administrador
@app.route("/inicioAdministrador")
def inicioAdministrador():
    tarea=False
    fr=[]
    ur=[]
    if("user" in session and "id" in session):
        ur = UsuarioRol.query.filter(UsuarioRol.usurol_id_usuario==session["id"]).all()
        if not ur is None:
            for aur in ur:
                if aur.usurol_id_rol == 1:
                    fr = FormularioRol.query.filter(FormularioRol.forrol_id_rol==1).all()
                    return render_template("usuario/inicioAdmi.html", fr=fr, ur=ur)
                else:
                    mensaje="Error de permisos" 
                    tarea=True 
        else:
            mensaje="No tiene asignado un rol por favor comunicarse con el servicio encargado 'Sistema'" 
            tarea=True 
    else:
        tarea=True
        mensaje="Debe primero iniciar Sesion"
    return render_template("frmCitaLogin.html",mensaje=mensaje, tarea=tarea)


@app.route("/rol", methods=['GET'])
def rol():
    tarea=False
    fr=[]
    ur=[]
    idRol = int(request.args.get('idRol'))
    if("user" in session and "id" in session):
        ur = UsuarioRol.query.filter(UsuarioRol.usurol_id_usuario==session["id"]).all()
        if ur!=None:
            fr = FormularioRol.query.filter(FormularioRol.forrol_id_rol==idRol).all()
            if idRol == 1:
                return render_template("usuario/inicioAdmi.html", fr=fr, ur=ur)
            elif idRol == 2:
                return render_template("usuario/inicio.html", fr=fr, ur=ur)
        else:
            mensaje="No tiene asignado un rol por favor comunicarse con el servicio encargado 'Sistema'" 
            tarea=True 
    else:
        tarea=True
        mensaje="Debe primero iniciar Sesion"
    return render_template("frmCitaLogin.html",mensaje=mensaje, tarea=tarea)

@app.route("/salir")
def salir():
    session.clear()
    tarea=True
    mensaje="Ha cerrado la sesión"
    return render_template("frmCitaLogin.html",mensaje=mensaje,tarea=tarea)
