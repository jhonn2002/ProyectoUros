from app import db

class Formulario(db.Model):
    __tablename__ = 'formulario' #Nombre de la tabla
    id_formulario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    for_nombre = db.Column(db.String(50), nullable=False)
    for_etiqueta = db.Column(db.String(30), nullable=False)
    for_ubicacion = db.Column(db.String(100), nullable=False)
    for_estado = db.Column(db.String(20),default='Activo', nullable=False)
    for_fecha_creacion = db.Column(db.DateTime, nullable=False)
    for_fecha_modificacion = db.Column(db.DateTime, nullable=False)
    for_id_usuario_creacion = db.Column(db.Integer, nullable=False)
    for_id_usuario_modificacion = db.Column(db.Integer, nullable=False)
    
    