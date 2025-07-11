from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .llave import Llave

class Cerradura_Puerta:

    def __init__(self, marca: str, material: str, tipo_cerradura: str):
        self.marca = marca
        self.material = material
        self.tipo_cerradura = tipo_cerradura
        self.llave: Optional["Llave"] = None