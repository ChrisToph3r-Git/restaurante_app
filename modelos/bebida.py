from modelos.producto import Producto

# Clase hija que hereda del Producto
class Bebida(Producto):

    # Constructor de la bebida
    def __init__(self, nombre, precio, disponible, volumen):
        super().__init__(nombre, precio, disponible)
        self.volumen = volumen

    # Sobrescribe el método de la clase padre
    def mostrar_informacion(self):
        print("--- BEBIDA ---")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.obtener_precio()}")
        print(f"Volumen: {self.volumen} ml")
        print(f"Disponible: {self.disponible}")
        print()