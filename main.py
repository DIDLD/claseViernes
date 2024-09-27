from fastapi import FastAPI
from app.database.configuration import engine
from app.api.models.modelosapp import Usuario
from app.api.rutas import rutas


from starlette.responses import RedirectResponse


#variable para administrar la aplicación
app=FastAPI()

#Activo el Api
@app.get("/")
def main():
    return RedirectResponse(url="/docs")

app.include_router(rutas)