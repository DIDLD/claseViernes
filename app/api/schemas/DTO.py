#librerías que ayudan 
#todas las respuestas deben tener datos, menos el id

from pydantic import BaseModel, Field

#Vamos a usar fechas entonces importamos desde datetime el date

from datetime import date


#DTO De petición y una de respuesta

class UsuarioDTOPeticion(BaseModel): #piden
    #str = string, el string se pone cuando se va a crear una tabla en la base de datos
    nombres: str
    edad: int
    telephone: str
    direccion: str
    correo: str
    fechade_registro: date 
    ciudad: str
    contrasena: str
    class Config: 
        orm_mode = True 



class UsuarioDTORespuesta(BaseModel): #respuesta

    id: int
    nombres: str
    telephone: str
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

    id_Gastos: int
    nombre: str
    descripcion: str
    ingresos: float    
    fecha: date


class CategoriaDTOPeticion(BaseModel):
    
    
    nombre_Categoria: str
    descripcion_Categoria: str
    fotoIcono: str
    class Config: 
        orm_mode = True


class CategoriaDTORespuesta(BaseModel):

    id_Categorias: int
    nombre_Categoria: str
    descripcion_Categoria: str
    fotoIcono: str


class MetodoPagoDTOPeticion(BaseModel):

  
    nombreMetodo: str
    descripcionMetodo: str 
    class Config: 
        orm_mode = True

class MetododeagoDTORespuesta(BaseModel):
    IDMetodoPago: int
    nombreMetodo: str
    descripcionMetodo: str




class FacturaDTOPeticion(BaseModel):

    monto_Factura: float
    fecha_Factura: date
    descripcion_Factura: str
    class Config: 
        orm_mode = True



class FacturaDTORespuesta(BaseModel):    

    ID_factura: int
    monto_Factura: float
    descripcion_Factura: str





