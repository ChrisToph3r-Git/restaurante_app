from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

# Crear el restaurante
restaurante = Restaurante()

while True:

    print("\n========================================")
    print("      SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("----------------------------------------")
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("----------------------------------------")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        try:
            nombre = input("Nombre del producto: ")
            categoria = input("Categoría: ")
            precio = input("Precio: ")

            respuesta = input("¿Está disponible? (s/n): ").lower()

            if respuesta == "s":
                disponible = True
            else:
                disponible = False

            nuevo_producto = Producto(nombre, categoria, precio, disponible)

            restaurante.agregar_producto(nuevo_producto)

            print("Producto registrado correctamente.")

        except ValueError as error:
            print(error)

    elif opcion == "2":

        restaurante.mostrar_productos()

    elif opcion == "3":

        nombre = input("Ingrese el nombre del producto: ")
        restaurante.buscar_producto(nombre)

    elif opcion == "4":

        try:
            id_cliente = int(input("ID del cliente: "))
            nombre = input("Nombre: ")
            correo = input("Correo: ")

            nuevo_cliente = Cliente(id_cliente, nombre, correo)

            restaurante.agregar_cliente(nuevo_cliente)

            print("Cliente registrado correctamente.")

        except ValueError:
            print("Error al registrar el cliente.")

    elif opcion == "5":

        restaurante.mostrar_clientes()

    elif opcion == "6":

        nombre = input("Ingrese el nombre del cliente: ")
        restaurante.buscar_cliente(nombre)

    elif opcion == "7":

        print("Programa finalizado.")
        break

    else:

        print("Opción no válida.")