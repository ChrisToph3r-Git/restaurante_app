# Sistema de Gestión de Restaurante

## Autor

Christopher Leonardo Paredes Jiménez

## Descripción

Este proyecto fue desarrollado en Python utilizando Programación Orientada a Objetos (POO). El sistema permite registrar productos y clientes de un restaurante aplicando conceptos fundamentales como clases, objetos, atributos, métodos, constructores, método especial **str**() y organización modular del software.

## Estructura del Proyecto

```text
restaurante_app/
├── modelos/
│   ├── producto.py
│   └── cliente.py
├── servicios/
│   └── restaurante.py
└── main.py
```

### modelos/

Contiene las clases que representan las entidades principales del sistema:

* Producto
* Cliente

### servicios/

Contiene la clase Restaurante encargada de administrar los productos y clientes registrados.

### main.py

Es el punto de inicio del programa. Aquí se crean los objetos y se ejecutan los métodos necesarios para demostrar el funcionamiento del sistema.

## Reflexión

La modularización permite organizar mejor el código, separar responsabilidades y facilitar el mantenimiento de los programas al dividir el proyecto en modelos, servicios y archivo principal, el sistema resulta más claro, reutilizable y escalable para futuros desarrollos.
