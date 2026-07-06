from modelos.producto import Producto

# Clase hija que hereda de Producto
class Platillo(Producto):

    # Constructor del platillo
    def __init__(self, nombre, precio, disponible, calorias):
        super().__init__(nombre, precio, disponible)
        self.calorias = calorias

    # Sobrescribe el método de la clase padre
    def mostrar_informacion(self):
        print("--- PLATILLO ---")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.obtener_precio()}")
        print(f"Calorías: {self.calorias}")
        print(f"Disponible: {self.disponible}")
        print()