from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.calculos import calcular_costo_tamales, calcular_ganancias

app = FastAPI()

class DatosSemanales(BaseModel):
    usuario: str
    precio_tamal: int = Field(gt=0)
    precio_tamal_platano: int = Field(gt=0)
    tamales: list[int]
    tamales_platano: list[int]


@app.post("/calcular")
def calcular(datos: DatosSemanales):
    total_tamales_regulares = calcular_costo_tamales(datos.tamales, datos.precio_tamal)
    total_tamales_platano = calcular_costo_tamales(datos.tamales_platano, datos.precio_tamal_platano)

    total_final = total_tamales_regulares + total_tamales_platano
    
    ganancia = calcular_ganancias(datos.tamales, datos.tamales_platano)
    
    return {"total_a_pagar":total_final, "ganancia":ganancia}