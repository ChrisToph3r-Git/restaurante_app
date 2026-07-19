from modelos.producto import Producto


class Bebida(Producto):
    """Clase que representa una bebida del restaurante."""

    def __init__(
        self,
        codigo,
        nombre,
        categoria,
        precio,
        tamano,
        tipo_envase
    ):
        super().__init__(
            codigo,
            nombre,
            categoria,
            precio
        )

        self.tamano = tamano
        self.tipo_envase = tipo_envase

    # Propiedad tamaño
    @property
    def tamano(self):
        return self._tamano

    @tamano.setter
    def tamano(self, valor):
        if not valor or valor.strip() == "":
            raise ValueError(
                "Error: El tamaño de la bebida no puede estar vacío."
            )
        self._tamano = valor

    # Propiedad tipo de envase
    @property
    def tipo_envase(self):
        return self._tipo_envase

    @tipo_envase.setter
    def tipo_envase(self, valor):
        if not valor or valor.strip() == "":
            raise ValueError(
                "Error: El tipo de envase no puede estar vacío."
            )
        self._tipo_envase = valor

    def mostrar_informacion(self):
        """Muestra los datos de la bebida."""

        print(
            f"Código: {self.codigo} | "
            f"Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f} | "
            f"Tamaño: {self.tamano} | "
            f"Tipo de envase: {self.tipo_envase}"
        )