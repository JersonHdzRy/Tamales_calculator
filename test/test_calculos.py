# test/test_calculos.py
import pytest
from app.calculos import calcular_costo_regulares

def test_costo_con_datos_validos():
    tamales = [3, 4, 6, 7]
    costo_unitario = 7

    resultado = calcular_costo_regulares(tamales, costo_unitario)

    assert resultado == 140   # (3+4+6+7) * 7, calculado a mano

def test_lista_vacia():
    tamales = []
    costo_unitario = 15

    with pytest.raises(ValueError):
        calcular_costo_regulares(tamales, costo_unitario)

def test_costo_unitario_vacio():
    tamales = [112,332,441,116,100]
    costo_unitario = 0

    with pytest.raises(ValueError):
            calcular_costo_regulares(tamales, costo_unitario)

def test_costo_unitario_None():
    tamales = [112,332,441,116,100]
    costo_unitario = None

    with pytest.raises(TypeError):
            calcular_costo_regulares(tamales, costo_unitario)

def test_costo_unitario_negativo():
    tamales = [112,332,441,116,100]
    costo_unitario = -21

    with pytest.raises(ValueError):
            calcular_costo_regulares(tamales, costo_unitario)

def test_tamales_negativos():
    tamales = [112,332,-441,116,100]
    costo_unitario = 15

    with pytest.raises(ValueError):
            calcular_costo_regulares(tamales, costo_unitario)

def test_tamales_None():
    tamales = [112,None,441,116,100]
    costo_unitario = 15

    with pytest.raises(TypeError):
            calcular_costo_regulares(tamales, costo_unitario)

def test_tamal_abc():
    tamales = [112,"abc",441,116,100]
    costo_unitario = 15

    with pytest.raises(TypeError):
            calcular_costo_regulares(tamales, costo_unitario)

def test_array_vacio():
    tamales = [112,[],441,116,100]
    costo_unitario = 15

    with pytest.raises(TypeError):
            calcular_costo_regulares(tamales, costo_unitario)

def test_precio_unitario_list():
    tamales = [112,113,441,116,100]
    costo_unitario = []

    with pytest.raises(TypeError):
            calcular_costo_regulares(tamales, costo_unitario)