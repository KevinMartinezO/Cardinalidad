from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .chasis import Chasis

class VIN:
    def __init__(self, codigo_vin: str, pais_origen: str, fabricante: str, año: int, numero_produccion: int):
        self.codigo_vin = codigo_vin
        self.pais_origen = pais_origen
        self.fabricante = fabricante
        self.año_modelo = año
        self.numero_produccion = numero_produccion
        self.chasis: Optional['Chasis'] = None