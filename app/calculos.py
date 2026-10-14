import logging

logger = logging.getLogger(__name__)

def calcular_costo_regulares(tamales: list[int], costo_unitario:int) -> int:
    if not tamales:
        raise ValueError("La lista de tamales esta vacia")
    
    logger.debug("La lista de tamales si tiene datos")
    logger.debug("Lista de tamales: %s", tamales)

    if not isinstance(costo_unitario,int) or isinstance(costo_unitario, bool):
        raise TypeError(f"{costo_unitario} es un numero invalido")
    if costo_unitario < 0:
        raise ValueError(f"El costo unitario no puede ser negativo: {costo_unitario}")
        
    for numero_tamales in tamales:
        if not isinstance(numero_tamales,int) or isinstance(numero_tamales, bool):
            raise TypeError(f"{numero_tamales} es un numero invalido")
        if numero_tamales <0:
            raise ValueError(f"La cantidad no puede ser negativa: {numero_tamales}")

    sumatoria_tamales = sum(tamales)
    costo_final = sumatoria_tamales * costo_unitario

    return costo_final



