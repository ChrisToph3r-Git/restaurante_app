from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

mi_restaurante = Restaurante()

# Creamos los platillos
platillo1 = Platillo("Hamburguesa", 6.50, True, 750)
platillo2 = Platillo("Pizza", 8.00, True, 900)

# Creamos las bebidas
bebida1 = Bebida("Coca Cola", 1.50, True, 500)
bebida2 = Bebida("Jugo Natural", 2.00, False, 350)

# Agregamos los productos al restaurante
mi_restaurante.agregar_producto(platillo1)
mi_restaurante.agregar_producto(platillo2)
mi_restaurante.agregar_producto(bebida1)
mi_restaurante.agregar_producto(bebida2)

# Mostrar todos los productos
mi_restaurante.mostrar_productos()

# Modificamos el precio de un producto
platillo1.cambiar_precio(7.00)

print("Precio actualizado:")
print(platillo1.obtener_precio())