import logging

logger = logging.getLogger('logger')

def calcular_costo_regulares(tamales: list[int], costo_unitario:int) -> int:
    if not tamales:
        raise Exception("La lista de tamales esta vacia")
    
    logger.info("La lista de tamales si tiene datos")
    logger.info(f"Lista de tamales: {tamales}")

    if not isinstance(costo_unitario,int):
        raise Exception(f"{costo_unitario} es un numero invalido")
        
    for numero_tamales in tamales:
        if not isinstance(numero_tamales,int):
            raise TypeError(f"{numero_tamales} es un numero invalido")
        if numero_tamales <0:
            raise ValueError(f"La cantidad no puede ser negativa: {numero_tamales}")

    sumatoria_tamales = sum(tamales)
    costo_final = sumatoria_tamales * costo_unitario

    return costo_final



