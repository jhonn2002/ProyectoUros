from app import db

class Usuario(db.Model): 
    __tablename__ = 'usuario' #Nombre de la tabla
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usu_id_persona = db.Column(db.Integer, db.ForeignKey('persona.id_persona'), nullable=False)
    usu_usuario = db.Column(db.String(100),nullable=False)
    usu_password = db.Column(db.String(100),nullable=False)
    usu_estado = db.Column(db.String(20),default='Activo', nullable=False)
    usu_fecha_activacion = db.Column(db.DateTime, nullable=False)
    usu_fecha_expiracion = db.Column(db.DateTime, nullable=False)
    usu_fecha_creacion = db.Column(db.DateTime, nullable=False)
    usu_fecha_modificacion = db.Column(db.DateTime, nullable=False)
    usu_id_usuario_creacion = db.Column(db.Integer, nullable=False)
    usu_id_usuario_modificacion = db.Column(db.Integer, nullable=False)
    
    usu_persona=db.relationship('Persona',backref=db.backref('usu_persona',lazy=True))