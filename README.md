# Sistema de Gestión de Restaurante

## Autor

Christopher Leonardo Paredes Jiménez

## Descripción

Este proyecto corresponde a la tarea práctica de la asignatura Programación Orientada a Objetos, consiste en el desarrollo de un sistema básico de gestión de restaurante utilizando Programación Orientada a Objetos (POO) en Python el sistema permite registrar productos y clientes mediante una estructura modular aplicando clases, objetos, atributos, métodos, constructores, listas e importaciones entre módulos.

## Estructura del Proyecto

```text
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py
```

### modelos/

Contiene las clases que representan las entidades principales del sistema:

- Producto
- Cliente

### servicios/

Contiene la clase `Restaurante`, encargada de administrar las listas de productos y clientes registrados mediante distintos métodos.

### main.py

Es el punto de inicio del programa. En este archivo se crean los objetos, se agregan al servicio principal y se muestra la información registrada en consola.

## Componentes técnicos aplicados

En el desarrollo del proyecto se aplicaron los siguientes conceptos:

- Programación Orientada a Objetos (POO).
- Organización modular mediante las carpetas `modelos` y `servicios`.
- Uso de constructores `__init__()`.
- Implementación del método especial `__str__()`.
- Uso de listas para almacenar múltiples objetos.
- Importación de módulos entre archivos.
- Identificadores descriptivos siguiendo las convenciones de Python (PascalCase y snake_case).

## Tipos de datos utilizados

Durante el desarrollo del proyecto se utilizaron los siguientes tipos de datos:

- `str`: para almacenar nombres, categorías y correos electrónicos.
- `int`: para almacenar el número telefónico del cliente.
- `float`: para representar el precio de los productos.
- `bool`: para indicar la disponibilidad de un producto y el estado del cliente.
- `list`: para almacenar múltiples objetos de tipo Producto y Cliente dentro del restaurante.

## Ejecución del programa

Para ejecutar el proyecto, abra una terminal dentro de la carpeta `restaurante_app` y ejecute el siguiente comando:

```bash
python main.py
```

## Reflexión

El uso de identificadores descriptivos tipos de datos adecuados y una estructura modular facilita la organización, comprensión y mantenimiento del código, ademas que permite desarrollar programas más claros y escalables, aplicando correctamente los principios fundamentales de la Programación Orientada a Objetos en Python.