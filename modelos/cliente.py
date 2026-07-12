from dataclasses import dataclass

@dataclass
class Cliente:
    """
    Clase que representa un cliente del restaurante.
    Se implementa utilizando el decorador @dataclass.
    """

    id_cliente: int
    nombre: str
    correo: str

    def mostrar_informacion(self):
        """Muestra la información del cliente."""
        print(f"ID: {self.id_cliente} | Nombre: {self.nombre} | Correo: {self.correo}")