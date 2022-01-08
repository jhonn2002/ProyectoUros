from app import app
from flask import request, render_template
import yagmail, os
from werkzeug.utils import secure_filename


@app.route("/citasEnLinea", methods=['POST'])
def citasEnLinea():

    #Declaro 3 variables 
    estado=False

    #Se guardan los valores que viene del formulario en las distintas varibles
    nombre = request.form['txtNombre']
    apellido=request.form['txtApellido']
    telefono = request.form['txtTelefono']
    direccion=request.form['txtDireccion']
    entidad = request.form['txtEntidad']
    fechaCita=request.form['dateCita']
    tipoCita = request.form['selectTipoCita']
    genero=request.form['selectGenero']
    fechaNacimiento = request.form['dateNacimiento']
    mensajeF=request.form['txtMensaje']
    correo=request.form['txtCorreo']
    corre="jfsanchez193@misena.edu.co"

    #Confirmo que las variables no esten vacias
    try:
        if nombre and apellido and telefono and direccion and entidad and fechaCita and tipoCita and genero and fechaNacimiento and mensajeF and correo:
            # Enviar Correo con archivo

                asunto=f'SOLICITUD DE CITAS EN LÍNEA'
                contenido=f"""
                          <table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;background:#ffffff;">
                            <tr>
                              <td align="center" style="padding:0;">
                                <table role="presentation" style="width:602px;border-collapse:collapse;border:1px solid #cccccc;border-spacing:0;text-align:left;">
                                  <tr>
                                    <td align="center" style="padding:40px 0 30px 0;">
                                      <img src="https://clinicauros.com/wp-content/uploads/2017/09/fachad1.jpg" alt="" width="300" style="height:auto;display:block;" />
                                    </td>
                                  </tr>
                                    <tr>
                                      <td style="padding:36px 30px 42px 30px;">
                                        <table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;">
                                          <tr>
                                            <td style="padding:0 0 36px 0;color:#153643;">
                                              <h1 style="font-size:24px;margin:0 0 20px 0;font-family:Arial,sans-serif;">INFORMACION DEL PACIENTE</h1>
                                              <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Nombre: {nombre}</p>
                                              <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Apellido: {apellido}</p>
                                              <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Telefono: {telefono}</p>
                                              <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Direccion: {direccion}</p>
                                              <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Entidad: {entidad}</p>
                                              <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Fecha de cita: {fechaCita}</p>
                                              <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Tipo de cita: {tipoCita}</p>
                                              <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Genero: {genero}</p>
                                              <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Fecha de nacimiento: {fechaNacimiento}</p>
                                              <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Mensaje: {mensajeF}</p>
                                              <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Correo: {correo}</p>
                                            </td>
                                          </tr>
                                        </table>
                                      </td>
                                    </tr>
                                </table>
                              </td>
                            </tr>
                          </table>
                        """
                try:
                    email=yagmail.SMTP('softcaf@gmail.com','softcaf2021')
                    email.send(to=corre, cc=correo, subject=asunto, contents=contenido)
                    estado=True     
                    mensaje=f'Su informacion fue enviada con exito'  
                except Exception as ex:
                    print(ex)  
        else:
            mensaje="Llenar los campos"
    except:
       mensaje="Error del sistema"
    
    return render_template("frmCitaLogin.html",mensaje=mensaje, tarea="agregarcitas", estado=estado)

@app.route("/trabajeConUros", methods=['POST'])
def trabajeConUros():
    #Declaro 3 variables 
    estado=False

    #Se guardan los valores que viene del formulario en las distintas varibles
    correo = request.form['txtCorreo']
    archivo=request.files['archivoTrabaje']
    corre="jfsanchez193@misena.edu.co"
    
    filename = secure_filename(archivo.filename)

    #Confirmo que las variables no esten vacias
    try:
        if correo and filename!="" :
            # Enviar Correo con archivo
          asunto=f'SOLICITUD DE EMPLEO'
          contenido=f"""
                        <table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;background:#ffffff;">
                          <tr>
                            <td align="center" style="padding:0;">
                              <table role="presentation" style="width:602px;border-collapse:collapse;border:1px solid #cccccc;border-spacing:0;text-align:left;">
                                <tr>
                                  <td align="center" style="padding:40px 0 30px 0;">
                                    <img src="https://clinicauros.com/wp-content/uploads/2017/09/fachad1.jpg" alt="" width="300" style="height:auto;display:block;" />
                                  </td>
                                </tr>
                                <tr>
                                  <td style="padding:36px 30px 42px 30px;">
                                    <table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;">
                                      <tr>
                                        <td style="padding:0 0 36px 0;color:#153643;">
                                          <h1 style="font-size:24px;margin:0 0 20px 0;font-family:Arial,sans-serif;">INFORMACION DEL EMPLEADO</h1>
                                          <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Correo: {correo}</p>
                                        </td>
                                      </tr>
                                    </table>
                                  </td>
                                </tr>
                              </table>
                            </td>
                          </tr>
                        </table>
                        """
          try:
              email=yagmail.SMTP('softcaf@gmail.com','softcaf2021')
              # Guardamos el archivo en el directorio "Archivos jpg"
              archivo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
              email.send(to=corre, cc=correo, subject=asunto, contents=contenido, attachments=[f'static/archivos/{filename}'])
              os.remove(os.path.join(app.config['UPLOAD_FOLDER'],filename))
              estado=True     
              mensaje=f'Su informacion fue enviada con exito'
          except Exception as ex:
              mensaje="Error no se puede finalizar su solicitud"
              estado=False    
        else:
            mensaje="Llenar los campos"
    except Exception as ex:
       mensaje=ex
    
    return render_template("trabajeConNosotros.html",mensaje=mensaje, tarea="trabajeConUros", estado=estado)
  
@app.route("/chequeoEjecutivos", methods=['POST'])
def chequeoEjecutivos():

    #Declaro 3 variables 
    estado=False

    #Se guardan los valores que viene del formulario en las distintas varibles
    nombre = request.form['txtNombre']
    apellido=request.form['txtApellido']
    telefono = request.form['txtTelefono']
    correo=request.form['txtCorreo']
    corre="jfsanchez193@misena.edu.co"

    #Confirmo que las variables no esten vacias
    try:
        if nombre and apellido :
            # Enviar Correo con archivo

                asunto=f'CHEQUEO EJECUTIVO'
                contenido=f"""
                          <table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;background:#ffffff;">
                            <tr>
                              <td align="center" style="padding:0;">
                                <table role="presentation" style="width:602px;border-collapse:collapse;border:1px solid #cccccc;border-spacing:0;text-align:left;">
                                  <tr>
                                    <td align="center" style="padding:40px 0 30px 0;">
                                      <img src="https://clinicauros.com/wp-content/uploads/2017/09/fachad1.jpg" alt="" width="300" style="height:auto;display:block;" />
                                    </td>
                                  </tr>
                                    <tr>
                                      <td style="padding:36px 30px 42px 30px;">
                                        <table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;">
                                          <tr>
                                            <td style="padding:0 0 36px 0;color:#153643;">
                                              <h1 style="font-size:24px;margin:0 0 20px 0;font-family:Arial,sans-serif;">CHEQUEO EJECUTIVO</h1>
                                              <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Nombre: {nombre}</p>
                                              <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Apellido: {apellido}</p>
                                              <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Telefono: {telefono}</p>
                                              <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Correo: {correo}</p>
                                            </td>
                                          </tr>
                                        </table>
                                      </td>
                                    </tr>
                                </table>
                              </td>
                            </tr>
                          </table>
                        """
                try:
                    email=yagmail.SMTP('softcaf@gmail.com','softcaf2021')
                    email.send(to=corre, cc=correo, subject=asunto, contents=contenido)
                    estado=True     
                    mensaje=f'Su informacion fue enviada con exito'  
                except Exception as ex:
                  mensaje="Error no se puede finalizar su solicitud"
        else:
          mensaje="Llenar los campos"
    except Exception as ex:
      mensaje="Error no se puede finalizar su solicitud"
    
    return render_template("chequeoEjecutivo.html",mensaje=mensaje, tarea="chequeoEjecutivos", estado=estado)

@app.route("/informacionPqr", methods=['POST'])
def informacionPqr():

    #Declaro 3 variables 
    estado=False

    #Se guardan los valores que viene del formulario en las distintas varibles
    tipoSolicitud = request.form['selectTipoSoli']
    nombre=request.form['txtNombre']
    apellido = request.form['txtServicio']
    numeroCedula=request.form['txtNumeroCedula']
    direccion = request.form['txtDireccion']
    barrio=request.form['txtBarrio']
    telefono = request.form['txtTelefono']
    correo=request.form['txtCorreo']
    entidad = request.form['txtEntidad']
    mensajeU=request.form['txtMensaje']
    corre="jfsanchez193@misena.edu.co"

    #Confirmo que las variables no esten vacias
    try:
        if nombre and apellido :
            # Enviar Correo con archivo

                asunto=f'PQR'
                contenido=f"""
                          <table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;background:#ffffff;">
                            <tr>
                              <td align="center" style="padding:0;">
                                <table role="presentation" style="width:602px;border-collapse:collapse;border:1px solid #cccccc;border-spacing:0;text-align:left;">
                                  <tr>
                                    <td align="center" style="padding:40px 0 30px 0;">
                                      <img src="https://clinicauros.com/wp-content/uploads/2017/09/fachad1.jpg" alt="" width="300" style="height:auto;display:block;" />
                                    </td>
                                  </tr>
                                    <tr>
                                      <td style="padding:36px 30px 42px 30px;">
                                        <table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;">
                                          <tr>
                                            <td style="padding:0 0 36px 0;color:#153643;">
                                              <h1 style="font-size:24px;margin:0 0 20px 0;font-family:Arial,sans-serif;">PQR</h1>
                                              <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Tipo De Solicitud: {tipoSolicitud}</p>
                                              <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Nombre: {nombre}</p>
                                              <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Apellido: {apellido}</p>
                                              <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Numero De Documento: {numeroCedula}</p>
                                              <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Dirrecion: {direccion}</p>
                                              <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Barrio: {barrio}</p>
                                              <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Telefono: {telefono}</p>
                                              <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Correo: {correo}</p>
                                              <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Entidad: {entidad}</p>
                                              <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Mensaje: {mensajeU}</p>
                                            </td>
                                          </tr>
                                        </table>
                                      </td>
                                    </tr>
                                </table>
                              </td>
                            </tr>
                          </table>
                        """
                try:
                    email=yagmail.SMTP('softcaf@gmail.com','softcaf2021')
                    email.send(to=corre, cc=correo, subject=asunto, contents=contenido)
                    estado=True     
                    mensaje=f'Su informacion fue enviada con exito'  
                except Exception as ex:
                  mensaje="Error no se puede finalizar su solicitud"
        else:
          mensaje="Llenar los campos"
    except Exception as ex:
      mensaje="Error no se puede finalizar su solicitud"
    
    return render_template("formularioPqr.html",mensaje=mensaje, tarea="informacionPqr", estado=estado)
