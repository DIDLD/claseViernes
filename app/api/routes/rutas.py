from fastapi import APIRouter, HTTPException  # enrutador del api
from sqlalchemy.orm import Session  # Para trabajar con la BD
from typing import List
from fastapi.params import Depends
from app.api.schemas.DTO import UsuarioDTOPeticion, UsuarioDTORespuesta, GastoDTOPeticion, GastoDTORespuesta, CategoriaDTOPeticion, CategoriaDTORespuesta, MetodoPagoDTORespuesta, MetodoPagoDTOPeticion, FacturaDTOPeticion, FacturaDTORespuesta

from app.api.models.modelosapp import Usuario, Gasto, Categoria, Factura, MetodoPago
from app.database.configuration import sessionLocal, engine

# Para que un api funcione debe tener un archivo enrutador

rutas = APIRouter()

# crear una función para establecer cuando yo quiera y necesite conexión hacia la base de datos

def getDatabase():
    basedatos = sessionLocal()
    try:
        yield basedatos
    except Exception as error:
        basedatos.rollback()
        raise error
    finally:
        basedatos.close()

# Programación de cada uno de los servicios que ofrecerá nuestra api

# Servicio para registrar o guardar un usuario en BD

@rutas.post("/usuarios")  # , response_model=UsuarioDTORespuesta) #pedir
def guardarUsuario(datosPeticion: UsuarioDTOPeticion, db: Session = Depends(getDatabase())):
    try:
        usuario = Usuario(
            nombres=datosPeticion.nombres,  # Para coincidir con el modelo
            correo=datosPeticion.correo,
            contrasena=datosPeticion.contrasena,  # Para coincidir con el modelo
            edad=datosPeticion.edad,
            telefono=datosPeticion.telephone,  # Para coincidir con el modelo
            ciudad=datosPeticion.ciudad,
            direccion=datosPeticion.direccion,
        )

        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return usuario  # {"message": "Usuario guardado correctamente", "usuario": usuario}
    
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error al registrar el usuario, mera gva")

@rutas.get("/usuarios," response_model = List[UsuarioDTORespuesta])  # mandar
def buscarUsuario(BD: Session = Depends(getDatabase)): # método buscar para hablar con la base de datos o establecer la conexión
    try:
        listaDeUsuarios = db.query(Usuario).all() #Vamos a usar una lista, hacemos que haga una búsqueda en la base de datos y busque todo
        return listaDeUsuarios


    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error al registrar el usuario, mera gva")





# Servicio para registrar o guardar un gasto en BD
@rutas.post("/gastos")
def guardarGasto(datosPeticion: GastoDTOPeticion, db: Session = Depends(getDatabase())):
    try:
        gasto = Gasto(
            nombre=datosPeticion.nombre,
            monto=datosPeticion.monto,
            fecha=datosPeticion.fecha,
            descripcion=datosPeticion.descripcion,
            ingresos=datosPeticion.ingresos
        )
        db.add(gasto)
        db.commit()
        db.refresh(gasto)
        return gasto  # {"message": "Gasto guardado correctamente", "gasto": gasto}
    
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error al registrar el usuario, mera gva")

@rutas.get("/gatos," response_model = List[UsuarioDTORespuesta])  # mandar
def buscarGasto(BD: Session = Depends(getDatabase)): # método buscar para hablar con la base de datos o establecer la conexión
    try:
        listaDeGastos = db.query(Gasto).all() #Vamos a usar una lista, hacemos que haga una búsqueda en la base de datos y busque todo
        return listaDeGastos


    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error al registrar el usuario, mera gva")
        


# Servicio para registrar o guardar una categoría en BD
@rutas.post("/categorias")  # Para coincidir con el modelo
def guardarCategoria(datosPeticion: CategoriaDTOPeticion, db: Session = Depends(getDatabase())):
    try:
        categoria = Categoria(
            nombre_categoria=datosPeticion.nombre_Categoria,  # Para coincidir con el modelo
            descripcion_categoria=datosPeticion.descripcion_Categoria,
            foto_icono=datosPeticion.fotoIcono
        )
        db.add(categoria)
        db.commit()
        db.refresh(categoria)
        return categoria  # {"message": "Categoría guardada correctamente", "categoria": categoria}
    
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error al registrar el usuario, mera gva")

@rutas.get("/categorias," response_model = List[UsuarioDTORespuesta])  # mandar
def buscarCategorias(BD: Session = Depends(getDatabase)): # método buscar para hablar con la base de datos o establecer la conexión
    try:
        listaDeCategorias = db.query(Categoria).all() #Vamos a usar una lista, hacemos que haga una búsqueda en la base de datos y busque todo
        return listaDeCategorias


    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error al registrar el usuario, mera gva")
        

# Servicio para registrar o guardar un método de pago en BD
@rutas.post("/metodos_pago")  # Para coincidir con el modelo
def guardarMetodoPago(datosPeticion: MetodoPagoDTOPeticion, db: Session = Depends(getDatabase())):
    try:
        metodo_pago = MetodoPago(
            nombre_metodo=datosPeticion.nombreMetodo,
            descripcion_metodo=datosPeticion.descripcionMetodo
        )
        db.add(metodo_pago)
        db.commit()
        db.refresh(metodo_pago)
        return metodo_pago  # {"message": "Método de pago guardado correctamente", "metodo_pago": metodo_pago}
    
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error al registrar el usuario, mera gva")

@rutas.get("/metodos_pagos," response_model = List[UsuarioDTORespuesta])  # mandar
def buscarMetodos_pagos(BD: Session = Depends(getDatabase)): # método buscar para hablar con la base de datos o establecer la conexión
    try:
        listaDeMetodos_pagos = db.query(MetodoPago).all() #Vamos a usar una lista, hacemos que haga una búsqueda en la base de datos y busque todo
        return listaDeMetodos_pagos


    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error al registrar el usuario, mera gva")
        
# Servicio para registrar o guardar una factura en BD
@rutas.post("/facturas")  # Para coincidir con el modelo
def guardarFactura(datosPeticion: FacturaDTOPeticion, db: Session = Depends(getDatabase())):
    try:
        factura = Factura(
            monto_factura=datosPeticion.monto_Factura,  # Para coincidir con el modelo
            fecha_factura=datosPeticion.fecha_Factura,
            descripcion_factura=datosPeticion.descripcion_Factura
        )
        db.add(factura)
        db.commit()
        db.refresh(factura)
        return factura  # {"message": "Factura guardada correctamente", "factura": factura}
    
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error al registrar el usuario, mera gva")

@rutas.get("/factura," response_model = List[UsuarioDTORespuesta])  # mandar
def buscarFactura(BD: Session = Depends(getDatabase)): # método buscar para hablar con la base de datos o establecer la conexión
    try:
        listaDeFactura = db.query(Factura).all() #Vamos a usar una lista, hacemos que haga una búsqueda en la base de datos y busque todo
        return listaDeFactura


    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error al registrar el usuario, mera gva")
        