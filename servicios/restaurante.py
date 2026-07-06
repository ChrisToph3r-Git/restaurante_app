# Clase que administra los productos del restaurante
class Restaurante:

    # Inicializa la lista de productos
    def __init__(self):
        self.productos = []

    # Agrega un producto a la lista
    def agregar_producto(self, producto):
        self.productos.append(producto)

    # Muestra todos los productos registrados
    def mostrar_productos(self):
        print("\n=== PRODUCTOS DEL RESTAURANTE ===\n")

        for producto in self.productos:
            producto.mostrar_informacion()