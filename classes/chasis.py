from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .vin import VIN

class Chasis:
    def __init__(self, numero_serie: str, fabricante: str , fecha_fabricacion: str, material: str, peso: float):
        self.numero_serie = numero_serie
        self.fabricante = fabricante
        self.fecha_fabricacion = fecha_fabricacion
        self.material = material
        self.peso = peso
        self.vin: Optional['VIN'] = None