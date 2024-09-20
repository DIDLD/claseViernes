from fastapi import APIRouter, HTTPException #enrutador del api
from sqlalchemy.orm import Session #Para trabajar con la BD
from typing import List
from fastapi.params import Depends
from app.api.schemas.DTO import UsuarioDTOPeticion,UsuarioDTORespuesta, GastoDTOPeticion, GastoDTORespuesta, CategoriaDTOPeticion, CategoriaDTORespuesta, MetododeagoDTORespuesta,MetodoPagoDTOPeticion, FacturaDTOPeticion, FacturaDTORespuesta

from app.api.models.modelosapp import Usuario, Gasto, Categoria, Factura, MetodoPago

from app.database.configuration import sessionLocal, engine


#Para que un api funcione debe tener un archivo enrutador

rutas = APIRouter()

#crear una funciópn para establecer cuando yo quiera y necesite conexión hacía la base de datos

def getDatabase():

    basedatos = sessionLocal()
    try:
        yield basedatos

    except Exception as error:

        basedatos.rollback()
        raise error
    

    finally:
        basedatos.close()


#Programación de cada uno de los servicios que ofrecerá nuestra api


#Servicio para registrar o guardar un usuario en BD


@rutas.post("/usuarios")#, response_model=UsuarioDTORespuesta) #pedir

def guardarUsuario(datosPeticion : UsuarioDTOPeticion, db: Session = Depends(getDatabase())) :

    try:
        usuario = Usuario(
            nombre = datosPeticion.nombres,
            email = datosPeticion.correo,
            contraseña = datosPeticion.contrasena,
            edad = datosPeticion.edad,
            telefono = datosPeticion.telephone,
            ciudad = datosPeticion.ciudad,
            direccion = datosPeticion.direccion,
            
        )

        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return usuario #{"message": "Usuario guardado correctamente", "usuario": usuario}
    
    except Exception as error:
        db.rollback()
        raise HTTPException()

@rutas.get("/usuarios") #mandar
def buscarUsuario():
    pass





#async def crear_usuario(usuario: UsuarioDTOPeticion, db: Session = Depends(getDatabase)):

    

    #db = sessionLocalConfig()

