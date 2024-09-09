from error import SubTipoInvalidoError


class Anuncio:
    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo):
        self._ancho = self.validar_dimensiones(ancho)
        self._alto = self.validar_dimensiones(alto)
        self._url_archivo = url_archivo
        self._sub_tipo = sub_tipo

    def validar_dimension(self, parametro: int):
        """Valida que el parámetro sea mayor a cero

        Args:
            parametro (int): dimension del anuncio a validar

        Returns:
            int: parametro (si es mayor a cero)
            int: 1 (si es menor a cero)
        """
        if parametro > 0:
            return parametro
        else:
            return 1

    @property
    def url_archivo(self):
        return self._url_archivo

    @property
    def url_clic(self):
        return self._url_clic

    @property
    def sub_tipo(self, subtipo):
        pass

    @staticmethod
    def mostrar_formatos(self):
        pass

    def comprimir_anuncio(self):
        """
        docstring
        """
        pass

    def redimensionar_anuncio(
        self,
    ):
        """
        docstring
        """
        pass


class Video(Anuncio):
    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo, duracion):
        self.duracion = duracion

    def comprimir_anuncio(self):
        """
        docstring
        """
        print("COMPRESION DE VIDEO NO IMPLEMENTADA AUN")

    def redimensionar_anuncio(
        self,
    ):
        """
        docstring
        """
        "RECORTE DE VIDEO NO IMPLEMENTADO AÚN"


class Display(Anuncio):
    def comprimir_anuncio(self):
        """
        docstring
        """
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        """
        docstring
        """
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")


class Social(Anuncio):

    def comprimir_anuncio(self):
        """
        docstring
        """
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        """
        docstring
        """
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NOIMPLEMENTADO AÚN")
