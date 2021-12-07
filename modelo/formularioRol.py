from app import db

class FormularioRol(db.Model): 
    __tablename__ = 'formulario_rol' #Nombre de la tabla
    id_formulario_rol = db.Column(db.Integer, primary_key=True, autoincrement=True)
    forrol_id_rol = db.Column(db.Integer, db.ForeignKey('rol.id_rol'), nullable=False)
    forrol_id_formulario = db.Column(db.Integer, db.ForeignKey('formulario.id_formulario'), nullable=False)
    forrol_estado = db.Column(db.String(20),default='Activo', nullable=False)
    forrol_fecha_creacion = db.Column(db.DateTime, nullable=False)
    forrol_fecha_modificacion = db.Column(db.DateTime, nullable=False)
    forrol_id_usuario_creacion = db.Column(db.Integer, nullable=False)
    forrol_id_usuario_modificacion = db.Column(db.Integer, nullable=False)

    forrol_rol = db.relationship('Rol',backref=db.backref('forrol_rol',lazy=True))
    forrol_formulario = db.relationship('Formulario',backref=db.backref('forrol_formulario',lazy=True))