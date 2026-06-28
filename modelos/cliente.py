class Cliente:

    def __init__(self, nombre: str, telefono: int, correo: str, activo: bool):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.activo = activo

    def mostrar_informacion(self):
        return f"Cliente: {self.nombre} | Correo: {self.correo} | Activo: {self.activo}"

    def __str__(self):
        return self.mostrar_informacion()