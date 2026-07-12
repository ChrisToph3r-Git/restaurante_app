# Clase que administra los productos y clientes del restaurante
class Restaurante:

    # Constructor
    def __init__(self):
        self.productos = []
        self.clientes = []

    # MÉTODOS DE PRODUCTOS
    def agregar_producto(self, producto):
        """Agrega un producto a la lista."""
        self.productos.append(producto)

    def mostrar_productos(self):
        """Muestra todos los productos."""
        if not self.productos:
            print("\nNo hay productos registrados.")
            return

        print("\n== PRODUCTOS ==")

        for producto in self.productos:
            producto.mostrar_informacion()

    def buscar_producto(self, nombre):
        """Busca un producto por nombre."""
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                producto.mostrar_informacion()
                return

        print("Producto no encontrado.")

    # METODOS DE CLIENTES
    def agregar_cliente(self, cliente):
        """Agrega un cliente."""
        self.clientes.append(cliente)

    def mostrar_clientes(self):
        """Muestra todos los clientes."""
        if not self.clientes:
            print("\nNo hay clientes registrados.")
            return

        print("\n== CLIENTES ==")

        for cliente in self.clientes:
            cliente.mostrar_informacion()

    def buscar_cliente(self, nombre):
        """Busca un cliente por nombre."""
        for cliente in self.clientes:
            if cliente.nombre.lower() == nombre.lower():
                cliente.mostrar_informacion()
                return

        print("Cliente no encontrado.")