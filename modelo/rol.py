from app import db

class Rol(db.Model):
    __tablename__ = 'rol' #Nombre de la tabla
    id_rol = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rol_nombre = db.Column(db.String(30), nullable=False, unique=True) 
    rol_estado = db.Column(db.String(15), nullable=False) 
    rol_fecha_creacion = db.Column(db.DateTime, nullable=False)
    rol_fecha_modificacion = db.Column(db.DateTime, nullable=False)
    rol_id_usuario_creacion = db.Column(db.Integer, nullable=False)
    rol_id_usuario_modificacion = db.Column(db.Integer, nullable=False)

