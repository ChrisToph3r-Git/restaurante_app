# Clase padre que representa un producto del restaurante
class Producto:

    # Constructor de la clase
    def __init__(self, nombre, precio, disponible=True):
        self.nombre = nombre
        self.__precio = precio      # Atributo encapsulado
        self.disponible = disponible

    # Aqui devolvera el precio del producto
    def obtener_precio(self):
        return self.__precio

    # Cambia el precio validando que sea mayor que cero
    def cambiar_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("Error: El precio debe ser mayor que cero.")

    # Este método será sobrescrito por las clases hijas
    def mostrar_informacion(self):
        print(f"Producto: {self.nombre}")
        print(f"Precio: ${self.__precio}")
        print(f"Disponible: {self.disponible}")