from modelos.producto import Producto
from servicios.restaurante import Restaurante

def main():
    # 1. Creamos el servicio principal
    mi_restaurante = Restaurante()

    # 2. Creamos los objetos Producto de forma correcta
    p1 = Producto("Pizza Familiar", 15.50, "Comida", True)
    p2 = Producto("Jugo de Naranja", 3.00, "Bebida", True)
    p3 = Producto("Hamburguesa Doble", 8.50, "Comida", True)

    # 3. Los agregamos al servicio usando las listas
    mi_restaurante.agregar_producto(p1)
    mi_restaurante.agregar_producto(p2)
    mi_restaurante.agregar_producto(p3)

    # 4. Mostramos la información organizada
    mi_restaurante.mostrar_productos()

if __name__ == "__main__":
    main()