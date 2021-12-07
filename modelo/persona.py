from app import db

class Persona(db.Model):
    __tablename__ = 'persona' #Nombre de la tabla
    id_persona = db.Column(db.Integer, primary_key=True, autoincrement=True)
    per_documento = db.Column(db.Integer, nullable=False, unique=True) 
    per_nombres = db.Column(db.String(50), nullable=False)
    per_apellidos = db.Column(db.String(50), nullable=False)
    per_correo = db.Column(db.String(50), nullable=False)
    per_genero = db.Column(db.String(20), nullable=False)
    per_telefono = db.Column(db.String(10), nullable=False)
    per_direcion = db.Column(db.String(20), nullable=False)
    per_fecha_nacimiento = db.Column(db.Date, nullable=False)
    per_fecha_creacion = db.Column(db.DateTime, nullable=False)
    per_fecha_modificacion = db.Column(db.DateTime, nullable=False)
    per_id_usuario_creacion = db.Column(db.Integer, nullable=False)
    per_id_usuario_modificacion = db.Column(db.Integer, nullable=False)