from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base

#Crear una instancia de la base de datos para crear tablas (variable)

Base = declarative_base()

#listado de modelos de la aplicación

#Modelo usuario


class Usuario(Base):


    __tablename__ = 'usuarios'

    id_Usuarios = Column(Integer, primary_key = True , autoincrement=True)
    nombres = Column(String (50))
    edad = Column(Integer )
    telephone = Column(String (50))
    correo = Column(String (50))
    contrasena = Column(String (50))
    fechade_Registro = Column(Date)
    ciudad = Column(String (50))

    #Cómo se configura tipo de dato nulltable y unique





#modelo de gasto

class Gasto(Base):
    
    __tablename__ = 'gastos'

    ID_Gastos = Column(Integer, primary_key = True, autoincrement= True)
    nombre = Column(String (50))
    monto = Column(Float)
    fecha = Column (Date)
    descripcion = Column (String (100))
    ingresos = Column(Float)


#modelo de categoría

class Categoria(Base):

    __tablename__ = 'categorias'

    ID_Categoria = Column(Integer, primary_key = True, autoincrement= True)
    nombre_Categoria = Column(String(50))
    descripcion_Categoria = Column (String (100))
    fotoIcono = Column (String (50))


#modelo de metodos de pago


class MetodoPago(Base):
    
    __tablename__ = 'metodo_pagos'
    IDMetodoPago = Column (Integer, primary_key= True, autoincrement= True) 
    nombreMetodo = Column (String(50))
    descripcionMetodo = Column (String (50))

#modelo de factura


class Factura(Base):

    __tablename__ = 'factura'

    ID_factura = Column(Integer, primary_key = True, autoincrement = True)
    monto_Factura = Column (Float)
    fecha_Factura = Column (Date)
    descripcion_Factura = Column (String (100))





#Relaciones entre tablas

