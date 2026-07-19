# Aplicación de los principios SOLID en un Restaurante en Python

## Autor

Christopher Leonardo Paredes Jiménez

---

## Descripción

Este proyecto fue desarrollado para la asignatura de Programación Orientada a Objetos. El sistema permite registrar productos, bebidas y clientes mediante un menú interactivo ejecutado desde consola.

El objetivo principal es demostrar la aplicación de los principios SOLID utilizando una estructura modular en Python. El proyecto está organizado en clases independientes que cumplen responsabilidades específicas, facilitando el mantenimiento y la ampliación del sistema.

---

## Estructura del proyecto

```text
restaurante_app/
├── modelos/
│   ├── producto.py
│   ├── bebida.py
│   └── cliente.py
├── servicios/
│   └── restaurante.py
├── main.py
└── README.md
```

---

## Responsabilidad de las clases

- **Producto:** Representa un producto del restaurante.
- **Bebida:** Hereda de Producto y agrega atributos como tamaño y tipo de envase.
- **Cliente:** Representa un cliente registrado.
- **Restaurante:** Administra los productos y clientes del sistema.
- **main.py:** Gestiona el menú interactivo y la entrada de datos.

---

## Relación entre Producto y Bebida

La clase Bebida hereda de Producto, por lo que puede utilizarse como un producto común y almacenarse en la misma colección del sistema.

---

## Principios SOLID aplicados

- **SRP:** Cada clase cumple una responsabilidad específica.
- **OCP:** El sistema se amplía mediante la clase Bebida sin modificar la lógica principal.
- **LSP:** Los objetos Bebida pueden utilizarse como objetos Producto.

---

## Menú interactivo

El sistema presenta el siguiente menú:

```text
========================================
      SISTEMA DE RESTAURANTE
========================================
1. Registrar producto
2. Registrar bebida
3. Registrar cliente
----------------------------------------
4. Listar productos
5. Listar clientes
----------------------------------------
6. Salir
```

Toda la información es ingresada por el usuario mediante input().

---

## Ejecución del programa

Ejecutar el archivo principal desde la terminal:

```bash
python main.py
```

---

## Reflexión

El desarrollo de este proyecto me permitió comprender la importancia de diseñar programas mantenibles y organizados utilizando Programación Orientada a Objetos. La aplicación de los principios SOLID facilita la reutilización del código, mejora la organización de las responsabilidades y permite ampliar las funcionalidades del sistema sin afectar los componentes ya implementados.

Además, pude comprender cómo la herencia y el polimorfismo contribuyen a desarrollar aplicaciones más flexibles y fáciles de mantener en proyectos modulares de Python.