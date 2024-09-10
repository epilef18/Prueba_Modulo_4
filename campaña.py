from error import LargoExcedidoError
from anuncio import Social, Display, Video
from datetime import date


class Campaña:
    def __init__(
        self, nombre: str, fecha_inicio: date, fecha_termino: date, anuncios: list
    ):
        if len(nombre) > 250:
            raise LargoExcedidoError("El nombre no puede tener más de 250 caracteres.")
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = [self.__instancia_anuncio(anuncio) for anuncio in anuncios]

    def __instancia_anuncio(self, anuncios: dict):
        tipo_anuncio = anuncios.get("tipo", "").lower()
        ancho = anuncios.get("ancho", 0)
        alto = anuncios.get("alto", 0)
        url_archivo = anuncios.get("url_archivo", "")
        url_clic = anuncios.get("url_clic", "")
        sub_tipo = anuncios.get("sub_tipo", "")
        duracion = anuncios.get("duracion", 0)

        if tipo_anuncio == "video":
            return Video(url_archivo, url_clic, sub_tipo, duracion)
        elif tipo_anuncio == "social":
            return Social(ancho, alto, url_clic, url_clic, sub_tipo)
        else:
            return Display(ancho, alto, url_clic, url_clic, sub_tipo)

    @property
    def nombre(self):
        """getter nombre"""
        return self.__nombre

    @property
    def anuncios(self):
        """getter anuncios"""
        return self.__anuncios

    @property
    def fecha_inicio(self):
        """getter fecha_inicio"""
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio: date):
        """setter fecha_inicio"""
        self.__fecha_inicio = fecha_inicio

    @property
    def fecha_termino(self):
        """getter fecha_termino"""
        return self.__fecha_termino

    @fecha_termino.setter
    def fecha_termino(self, fecha_termino: date):
        """setter fecha_termino"""
        self.__fecha_termino = fecha_termino

    def __str__(self):
        for anuncio in self.__anuncios:
            return (
                f"Nombre de la campaña: {self.__nombre}\n"
                f"Fecha Inicio: {self.__fecha_inicio}\n"
                f"Fecha Término: {self.__fecha_termino}\n"
                f"Anuncios: {self.__anuncios.video} Video, {self.__anuncios.display} Display, {self.__anuncios.social}"
            )
