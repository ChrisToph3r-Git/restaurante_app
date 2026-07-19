from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


restaurante = Restaurante()


# ============================
# FUNCIONES DEL MENÚ
# ============================

def mostrar_menu():

    print("\n========================================")
    print("      SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("----------------------------------------")
    print("4. Listar productos")
    print("5. Listar clientes")
    print("----------------------------------------")
    print("6. Salir")


def registrar_producto():

    try:
        codigo = input("Código del producto: ")
        nombre = input("Nombre del producto: ")
        categoria = input("Categoría: ")
        precio = input("Precio: ")

        nuevo_producto = Producto(
            codigo,
            nombre,
            categoria,
            precio
        )

        restaurante.agregar_producto(nuevo_producto)

        print("Producto registrado correctamente.")

    except ValueError as error:
        print(error)


def registrar_bebida():

    try:
        codigo = input("Código de la bebida: ")
        nombre = input("Nombre de la bebida: ")
        categoria = input("Categoría: ")
        precio = input("Precio: ")
        tamano = input("Tamaño (por ejemplo, 500 ml): ")
        tipo_envase = input("Tipo de envase: ")

        nueva_bebida = Bebida(
            codigo,
            nombre,
            categoria,
            precio,
            tamano,
            tipo_envase
        )

        restaurante.agregar_producto(nueva_bebida)

        print("Bebida registrada correctamente.")

    except ValueError as error:
        print(error)


def registrar_cliente():

    try:
        id_cliente = int(input("ID del cliente: "))
        nombre = input("Nombre: ")
        correo = input("Correo electrónico: ")

        nuevo_cliente = Cliente(
            id_cliente,
            nombre,
            correo
        )

        restaurante.agregar_cliente(nuevo_cliente)

        print("Cliente registrado correctamente.")

    except ValueError as error:
        print(error)


def listar_productos():

    restaurante.mostrar_productos()


def listar_clientes():

    restaurante.mostrar_clientes()


# ============================
# PROGRAMA PRINCIPAL
# ============================

while True:

    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        registrar_producto()

    elif opcion == "2":

        registrar_bebida()

    elif opcion == "3":

        registrar_cliente()

    elif opcion == "4":

        listar_productos()

    elif opcion == "5":

        listar_clientes()

    elif opcion == "6":

        print("Programa finalizado.")
        break

    else:

        print("Opción no válida.")