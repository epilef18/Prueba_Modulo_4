from error import SubTipoInvalidoError


class Anuncio:
    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo):
        self.__ancho = self.validar_dimensiones(ancho)
        self.__alto = self.validar_dimensiones(alto)
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo

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
        return self.__url_archivo

    @url_archivo.setter
    def url_archivo(self, url_archivo):
        self.__url_archivo = url_archivo

    @property
    def url_clic(self):
        return self.__url_clic

    @url_clic.setter
    def url_clic(self, url_clic):
        self.__url_clic = url_clic

    @property
    def sub_tipo(self, subtipo):
        return self.__sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, parametro):
        if parametro not in self.SUB_TIPOS:
            raise SubTipoInvalidoError(f"sub tipo {parametro} inválido.")
        self.__sub_tipo = parametro

    @staticmethod
    def mostrar_formatos(self):
        for formato in [Video, Display, Social]:
            print(f"FORMATO {formato.FORMATO}:")
            print("==========")
            for subtipo, i in formato.SUB_TIPOS:
                print(f"{i}- {subtipo}")

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
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")

    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo, duracion):
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo)
        self.duracion = self.validar_video(duracion)

    def validar_video(self, parametro: int):
        if parametro > 0:
            return parametro
        else:
            return 5

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
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")

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
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")

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
