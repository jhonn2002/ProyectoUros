from app import app
from flask import render_template

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

@app.route('/cuidadosIntensivos')
def cuidadosIntensivos():
    return render_template('cuidadosIntensivos.html')

@app.route('/otros')
def otros():
    return render_template('otros.html')

@app.route('/noticiaSaludable')
def noticiaSaludable():
    return render_template('noticiaSaludable.html')

@app.route('/tratamientoDeDatos')
def tratamientoDeDatos():
    return render_template('tratamientoDeDatos.html')
