from error import LargoExcedidoError


class Campaña:
    def __init__(self, nombre: str, fecha_inicio, fecha_termino, anuncios):
        if len(nombre) > 250:
            raise LargoExcedidoError
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
        self._anuncios = self._crear_anuncios(anuncios)

    def crear_anuncios(self, anuncios):
        pass
