# test/test_calculos.py
from app.calculos import calcular_costo_regulares

def test_costo_con_datos_validos():
    tamales = [3, 4, 6, 7]
    costo_unitario = 7

    resultado = calcular_costo_regulares(tamales, costo_unitario)

    assert resultado == 140   # (3+4+6+7) * 7, calculado a mano