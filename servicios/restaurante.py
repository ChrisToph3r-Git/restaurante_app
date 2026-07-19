# Clase que administra los productos y clientes del restaurante
class Restaurante:
    """Clase encargada de administrar los productos y clientes."""

    def __init__(self):
        self.productos = []
        self.clientes = []

    # ============================
    # MÉTODOS DE PRODUCTOS
    # ============================

    def agregar_producto(self, producto):
        """Agrega un producto si su código no está repetido."""

        for producto_existente in self.productos:
            if producto_existente.codigo == producto.codigo:
                raise ValueError(
                    "Error: El código del producto ya existe."
                )

        self.productos.append(producto)

    def mostrar_productos(self):
        """Muestra todos los productos registrados."""

        if not self.productos:
            print("\nNo hay productos registrados.")
            return

        print("\n== PRODUCTOS REGISTRADOS ==")

        for producto in self.productos:
            producto.mostrar_informacion()

    # ============================
    # MÉTODOS DE CLIENTES
    # ============================

    def agregar_cliente(self, cliente):
        """Agrega un cliente si su identificación no está repetida."""

        for cliente_existente in self.clientes:
            if cliente_existente.id_cliente == cliente.id_cliente:
                raise ValueError(
                    "Error: El ID del cliente ya existe."
                )

        self.clientes.append(cliente)

    def mostrar_clientes(self):
        """Muestra todos los clientes registrados."""

        if not self.clientes:
            print("\nNo hay clientes registrados.")
            return

        print("\n== CLIENTES REGISTRADOS ==")

        for cliente in self.clientes:
            cliente.mostrar_informacion()