# Sistema de Gestión de Restaurante

## Autor

**Christopher Leonardo Paredes Jiménez**

---

## Descripción

Este proyecto corresponde a la tarea práctica de la asignatura **Programación Orientada a Objetos**. Consiste en el desarrollo de un sistema básico de gestión de productos de un restaurante utilizando Programación Orientada a Objetos (POO) en Python el sistema permite registrar y administrar productos mediante una estructura modular, aplicando los principios de *herencia, encapsulación y polimorfismo*, además del uso de clases, objetos, constructores, listas e importaciones entre módulos.

---

## Estructura del Proyecto

```text
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── platillo.py
│   └── bebida.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
├── main.py
└── README.md
```

---

## Descripción de las carpetas

### modelos/

Contiene las clases principales del sistema:

- **Producto:** Clase padre que representa un producto del restaurante.
- **Platillo:** Clase hija que hereda de Producto y agrega el atributo de calorías.
- **Bebida:** Clase hija que hereda de Producto y agrega el atributo de volumen.

### servicios/

Contiene la clase **Restaurante**, encargada de administrar la lista de productos registrados mediante distintos métodos.

### main.py

Es el punto de inicio del programa, en este archivo se crean los objetos, se agregan al servicio principal y se muestra la información registrada en consola.

---

## Relación de herencia

La clase **Producto** es la clase padre del sistema.

Las clases **Platillo** y **Bebida** heredan de ella mediante el uso de `super()`, reutilizando los atributos comunes como nombre, precio y disponibilidad, además de incorporar atributos específicos propios de cada tipo de producto.

---

## Encapsulación

Se aplicó encapsulación al atributo **__precio** de la clase **Producto** para proteger el acceso directo a la información.

Para manipular este atributo se implementaron los métodos:

- `obtener_precio()`
- `cambiar_precio()`

El método `cambiar_precio()` valida que el nuevo precio sea mayor que cero antes de realizar la modificación.

---

## Polimorfismo

El método `mostrar_informacion()` fue sobrescrito en las clases **Platillo** y **Bebida**, permitiendo que cada objeto muestre información diferente según su tipo cuando el programa recorre la lista de productos del restaurante.

---

## Componentes técnicos aplicados

En el desarrollo del proyecto se aplicaron los siguientes conceptos:

- Programación Orientada a Objetos (POO).
- Organización modular mediante las carpetas `modelos` y `servicios`.
- Herencia entre clases.
- Encapsulación de atributos.
- Polimorfismo mediante sobrescritura de métodos.
- Uso de constructores `__init__()`.
- Utilización de `super()`.
- Uso de listas para almacenar múltiples objetos.
- Importación de módulos entre archivos.
- Identificadores descriptivos siguiendo las convenciones de Python (PascalCase y snake_case).

---

## Tipos de datos utilizados

Durante el desarrollo del proyecto se utilizaron los siguientes tipos de datos:

- `str`: para almacenar nombres de productos.
- `float`: para representar el precio de los productos.
- `bool`: para indicar la disponibilidad de los productos.
- `int`: para representar las calorías de los platillos y el volumen de las bebidas.
- `list`: para almacenar los objetos registrados dentro del restaurante.

---

## Ejecución del programa

Para ejecutar el proyecto, abra una terminal dentro de la carpeta `restaurante_app` y ejecute el siguiente comando:

```bash
python main.py
```

---

## Reflexión

La aplicación de los principios de herencia, encapsulación y polimorfismo permitió desarrollar un sistema más organizado, reutilizable y fácil de mantener además que la estructura modular facilita la comprensión del código y demuestra cómo la Programación Orientada a Objetos contribuye al desarrollo de aplicaciones escalables y bien estructuradas en Python.