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
        raise HTTPException()

@rutas.get("/usuarios")  # mandar
def buscarUsuario():
    pass

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
        raise HTTPException()

@rutas.get("/gastos")  # mandar
def buscarGasto():
    pass

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
        raise HTTPException()

@rutas.get("/categorias")  # mandar
def buscarCategoria():
    pass

# Servicio para registrar o guardar un método de pago en BD
@rutas.post("/metodos-pago")  # Para coincidir con el modelo
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
        raise HTTPException()

@rutas.get("/metodos-pago")  # mandar
def buscarMetodoPago():
    pass

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
        raise HTTPException()

@rutas.get("/facturas")  # mandar
def buscarFactura():
    pass
