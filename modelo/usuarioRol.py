from app import db

class UsuarioRol(db.Model): 
    __tablename__ = 'usuario_rol' #Nombre de la tabla
    id_usuario_rol = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usurol_id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    usurol_id_rol = db.Column(db.Integer, db.ForeignKey('rol.id_rol'), nullable=False)
    usurol_estado = db.Column(db.String(20),default='Activo', nullable=False)
    usurol_fecha_creacion = db.Column(db.DateTime, nullable=False)
    usurol_fecha_modificacion = db.Column(db.DateTime, nullable=False)
    usurol_id_usuario_reacion = db.Column(db.Integer, nullable=False)
    usurol_id_usuario_modificacion = db.Column(db.Integer, nullable=False)
    
    usurol_rol = db.relationship('Rol',backref=db.backref('usurol_rol',lazy=True))
    usurol_usuario = db.relationship('Usuario',backref=db.backref('usurol_usuario',lazy=True))