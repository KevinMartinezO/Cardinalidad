from classes.partida_nacimiento import Partida_Nacimiento
from classes.persona import Persona

if __name__ == "__main__":

    partida=Partida_Nacimiento(20022, "Juan Perez", "01-01-2000", "Tegucigalpa")
    persona=Persona(partida)

    print("Número de registro: ",partida.numero_registro)
    print("Nombre: ", persona.nombre)
