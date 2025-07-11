from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .cerradura_puerta import Cerradura_Puerta

class Llave:
    def __init__(self, marca: str, material: str, tamaño: str):
        self.marca = marca
        self.material = material
        self.tamaño = tamaño
        self.cerradura_puerta: Optional['Cerradura_Puerta'] = None