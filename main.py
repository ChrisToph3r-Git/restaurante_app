from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

producto1 = Producto("Pizza Familiar", 15.50, "Comida")
producto2 = Producto("Jugo de Naranja", 3.00, "Bebida")
producto3 = Producto("Hamburguesa Doble", 8.50, "Comida")

cliente1 = Cliente("Christopher Paredes", "0991234567")
cliente2 = Cliente("Alex González", "0987654321")

restaurante = Restaurante()

restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)
restaurante.agregar_producto(producto3)

restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)

print("== PRODUCTOS DEL RESTAURANTE ==")
restaurante.mostrar_productos()

print("\n== CLIENTES REGISTRADOS ==")
restaurante.mostrar_clientes()