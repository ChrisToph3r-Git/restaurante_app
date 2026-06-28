from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def main():

    mi_restaurante = Restaurante()

    p1 = Producto("Pizza Familiar", 15.50, "Comida", True)
    p2 = Producto("Jugo de Naranja", 3.00, "Bebida", True)

    c1 = Cliente("Juan Pérez", 987654321, "juan@gmail.com", True)
    c2 = Cliente("María López", 912345678, "maria@gmail.com", True)

    mi_restaurante.agregar_producto(p1)
    mi_restaurante.agregar_producto(p2)

    mi_restaurante.agregar_cliente(c1)
    mi_restaurante.agregar_cliente(c2)

    print("=== PRODUCTOS ===")
    mi_restaurante.mostrar_productos()

    print("\n=== CLIENTES ===")
    mi_restaurante.mostrar_clientes()

if __name__ == "__main__":
    main()