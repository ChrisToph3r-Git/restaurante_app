#  Organización modular de un sistema orientado a objetos en Python

## Autor

**Christopher Leonardo Paredes Jiménez**

---

## Descripción

Este proyecto fue desarrollado para la asignatura de Programación Orientada a Objetos, el sistema permite registrar, listar y buscar productos y clientes de un restaurante mediante un menú interactivo en consola.

Durante el desarrollo se aplican conceptos como constructores, encapsulación con `@property` y `@setter`, el uso de `@dataclass`, programación modular y la creación de objetos a partir de datos ingresados por el usuario.

---

## Estructura del proyecto

```text
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
├── main.py
└── README.md
```

---

## Descripción de las carpetas

### modelos/

Contiene las clases principales del sistema.

- **Producto:** representa los productos del restaurante y utiliza constructor, `@property` y `@setter`.
- **Cliente:** representa los clientes registrados y está implementado mediante `@dataclass`.

### servicios/

Contiene la clase *Restaurante*, encargada de administrar las listas de productos y clientes, además de registrar, listar y buscar información.

### main.py

Es el punto de inicio del programa. Presenta un menú interactivo que permite al usuario ingresar datos desde el teclado y crear los objetos del sistema.

---

## Uso del constructor

La clase **Producto** utiliza el constructor `__init__()` para crear cada producto con su nombre, categoría, precio y disponibilidad, cada vez que el usuario registra un producto desde el menú, se crea un nuevo objeto utilizando este constructor.

---

## Uso de @property y @setter

Se utilizaron `@property` y `@setter` para controlar el acceso a los atributos del producto.

Las validaciones implementadas permiten comprobar que:

- El nombre no esté vacío.
- La categoría no esté vacía.
- El precio sea mayor que cero.

---

## Uso de @dataclass

La clase **Cliente** fue implementada utilizando `@dataclass`, lo que permite crear automáticamente el constructor y facilita el manejo de los datos del cliente.

---

## Menú interactivo

El programa presenta un menú que permite realizar las siguientes operaciones:

- Registrar productos.
- Listar productos.
- Buscar productos.
- Registrar clientes.
- Listar clientes.
- Buscar clientes.
- Salir del sistema.

Toda la información es ingresada mediante `input()`, evitando utilizar datos definidos directamente en el código.

---

## Ejecución del programa

Desde la terminal, ubicarse dentro de la carpeta del proyecto y ejecutar:

```bash
python main.py
```

---

## Reflexión

Este proyecto me permitió comprender mejor cómo los constructores permiten crear objetos a partir de los datos ingresados por el usuario. Además, aprendí la utilidad de `@property`, `@setter` y `@dataclass`, así como la importancia de utilizar un menú interactivo para facilitar el registro y la búsqueda de información. Todo esto me ayudó a organizar mejor el código y a aplicar los principios de la Programación Orientada a Objetos mediante una estructura modular.