"""Funciones para calcular el precio total de la venta de los tamales"""
import logging

logger = logging.getLogger(__name__)

def calcular_costo_regulares(tamales: list[int], costo_unitario:int) -> int:
    """
    Esta funcion se usa para calcular el costo de los tamales 'normales' (entiendase por normales los tamales de hoja de maiz)

    Argumentos:
    tamales: lista de numeros enteros correspondiente a la cantidad de tamales vendidos por dia
    costo unitario: cantidad a pagar por tamal

    Retorna:
    costo_final: es la cantidad de dinero que se tiene que pagar
    por los tamales vendidos en la semana

    Errores:
    ValueError: en caso de que la lista de tamales este vacia, que el costo 
    unitario sea negativo o 0, que en un dia de la semana se haya introducido una cantidad que sea negativa,
    resulta en este error

    TypeError: este error resulta porque se detecto que alguno de los elementos de la lista de tamales 
    no es un numero entero o porque el costo unitario es menor o igual a 0

    """
    if not tamales:
        raise ValueError("La lista de tamales esta vacia")
    
    logger.debug("La lista de tamales si tiene datos")
    logger.debug("Lista de tamales: %s", tamales)

    if not isinstance(costo_unitario,int) or isinstance(costo_unitario, bool):
        raise TypeError(f"{costo_unitario} es un numero invalido")
    if costo_unitario <= 0:
        raise ValueError(f"El costo unitario no puede ser negativo: {costo_unitario}")
        
    for numero_tamales in tamales:
        if not isinstance(numero_tamales,int) or isinstance(numero_tamales, bool):
            raise TypeError(f"{numero_tamales} es un numero invalido")
        if numero_tamales <0:
            raise ValueError(f"La cantidad no puede ser negativa: {numero_tamales}")

    sumatoria_tamales = sum(tamales)
    costo_final = sumatoria_tamales * costo_unitario

    return costo_final



