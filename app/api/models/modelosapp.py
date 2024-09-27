from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Crear una instancia de la base de datos para crear tablas (variable)
Base = declarative_base()

# Listado de modelos de la aplicación

# Modelo Usuario
class Usuario(Base):
    __tablename__ = 'usuarios'

    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nombres = Column(String(50))
    edad = Column(Integer)
    telefono = Column(String(50))
    correo = Column(String(50))
    contrasena = Column(String(50))
    fecha_registro = Column(Date)
    ciudad = Column(String(50))

# Modelo Gasto
class Gasto(Base):
    __tablename__ = 'gastos'

    id_gasto = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50))
    monto = Column(Float)
    fecha = Column(Date)
    descripcion = Column(String(100))
    ingresos = Column(Float)

# Modelo Categoría
class Categoria(Base):
    __tablename__ = 'categorias'

    id_categoria = Column(Integer, primary_key=True, autoincrement=True)
    nombre_categoria = Column(String(50))
    descripcion_categoria = Column(String(100))
    foto_icono = Column(String(50))

# Modelo Método de Pago
class MetodoPago(Base):
    __tablename__ = 'metodos_pago'
    id_metodo_pago = Column(Integer, primary_key=True, autoincrement=True)
    nombre_metodo = Column(String(50))
    descripcion_metodo = Column(String(50))

# Modelo Factura
class Factura(Base):
    __tablename__ = 'facturas'

    id_factura = Column(Integer, primary_key=True, autoincrement=True)
    monto_factura = Column(Float)
    fecha_factura = Column(Date)
    descripcion_factura = Column(String(100))
