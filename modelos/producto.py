class Producto:
    """Clase que representa un producto del restaurante."""

    def __init__(self, nombre, categoria, precio, disponible=True):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible

    # Propiedad: nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or valor.strip() == "":
            raise ValueError("Error: El nombre del producto no puede estar vacío.")
        self._nombre = valor

    # Propiedad: categoría
    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, valor):
        if not valor or valor.strip() == "":
            raise ValueError("Error: La categoría no puede estar vacía.")
        self._categoria = valor

    # Propiedad: precio
    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        try:
            valor = float(valor)
        except ValueError:
            raise ValueError("Error: El precio debe ser un número.")

        if valor <= 0:
            raise ValueError("Error: El precio debe ser mayor que cero.")

        self._precio = valor

    def mostrar_informacion(self):
        """Muestra los datos del producto."""
        estado = "Disponible" if self.disponible else "Agotado"
        print(
            f"Producto: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f} | "
            f"Estado: {estado}"
        )
        