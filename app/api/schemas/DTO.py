#librerías que ayudan 
#todas las respuestas deben tener datos, menos el id

from pydantic import BaseModel
from datetime import date  # Vamos a usar fechas entonces importamos desde datetime el date


#DTO De petición y una de respuesta

class UsuarioDTOPeticion(BaseModel):  # piden
    #str = string, el string se pone cuando se va a crear una tabla en la base de datos
    nombres: str
    edad: int
    telefono: str  # Cambiado para coincidir con el modelo
    direccion: str
    correo: str
    fecha_registro: date  # Cambiado para coincidir con el modelo
    ciudad: str
    contrasena: str
    class Config:
        orm_mode = True


class UsuarioDTORespuesta(BaseModel):  # respuesta
    id_usuario: int  
    nombres: str
    telefono: str  
    correo: str
    edad: int
    ciudad: str


class GastoDTOPeticion(BaseModel):
    nombre: str
    monto: float
    fecha: date
    descripcion: str
    ingresos: float
    class Config:
        orm_mode = True


class GastoDTORespuesta(BaseModel):
    id_gasto: int  
    nombre: str
    descripcion: str
    ingresos: float
    fecha: date


class CategoriaDTOPeticion(BaseModel):
    nombre_categoria: str  
    descripcion_categoria: str  
    foto_icono: str  
    class Config:
        orm_mode = True


class CategoriaDTORespuesta(BaseModel):
    id_categoria: int  
    nombre_categoria: str  
    descripcion_categoria: str  
    foto_icono: str  


class MetodoPagoDTOPeticion(BaseModel):
    nombre_metodo: str  
    descripcion_metodo: str  
    class Config:
        orm_mode = True


class MetodoPagoDTORespuesta(BaseModel):
    id_metodo_pago: int  
    nombre_metodo: str  
    descripcion_metodo: str  


class FacturaDTOPeticion(BaseModel):
    monto_factura: float  
    fecha_factura: date  
    descripcion_factura: str  
    class Config:
        orm_mode = True


class FacturaDTORespuesta(BaseModel):
    id_factura: int  
    monto_factura: float  
    descripcion_factura: str  
