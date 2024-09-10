from error import SubTipoInvalidoError


class Anuncio:
    """
    Clase base para anuncios.

    Atributos:
        ancho (int): Ancho del anuncio.
        alto (int): Alto del anuncio.
        url_archivo (str): URL del archivo del anuncio.
        url_clic (str): URL de clic del anuncio.
        sub_tipo (str): Subtipo del anuncio.
    """

    def __init__(
        self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str
    ):
        """
        Inicializa una nueva instancia de Anuncio.

        Args:
            ancho (int): Ancho del anuncio.
            alto (int): Alto del anuncio.
            url_archivo (str): URL del archivo del anuncio.
            url_clic (str): URL de clic del anuncio.
            sub_tipo (str): Subtipo del anuncio.
        """
        self.__ancho = self.validar_dimension(ancho)
        self.__alto = self.validar_dimension(alto)
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.sub_tipo = sub_tipo

    def validar_dimension(self, parametro: int) -> int:
        """
        Valida que el parámetro de dimensión sea mayor a cero.

        Args:
            parametro (int): Dimensión del anuncio a validar.

        Returns:
            int: Parámetro (si es mayor a cero).
            int: 1 (si es menor a cero).
        """
        return parametro if parametro > 0 else 1

    @property
    def url_archivo(self) -> str:
        """
        Getter de la URL del archivo del anuncio.

        Returns:
            str: URL del archivo del anuncio.
        """
        return self.__url_archivo

    @url_archivo.setter
    def url_archivo(self, url_archivo: str):
        """
        Setter de la URL del archivo del anuncio.

        Args:
            url_archivo (str): Nueva URL del archivo del anuncio.
        """
        self.__url_archivo = url_archivo

    @property
    def url_clic(self) -> str:
        """
        Getter de la URL de clic del anuncio.

        Returns:
            str: URL de clic del anuncio.
        """
        return self.__url_clic

    @url_clic.setter
    def url_clic(self, url_clic: str):
        """
        Setter de la URL de clic del anuncio.

        Args:
            url_clic (str): Nueva URL de clic del anuncio.
        """
        self.__url_clic = url_clic

    @property
    def sub_tipo(self) -> str:
        """
        Getter del subtipo del anuncio.

        Returns:
            str: Subtipo del anuncio.
        """
        return self.__sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, parametro: str):
        """
        Setter del subtipo del anuncio.

        Args:
            parametro (str): Nuevo subtipo del anuncio.

        Raises:
            SubTipoInvalidoError: Si el subtipo no es válido.
        """
        if parametro not in self.SUB_TIPOS:
            raise SubTipoInvalidoError(f"Subtipo {parametro} inválido.")
        self.__sub_tipo = parametro

    @staticmethod
    def mostrar_formatos():
        """
        Muestra los formatos y subtipos de los anuncios disponibles.
        """
        for formato in [Video, Display, Social]:
            print(f"FORMATO {formato.FORMATO}:")
            print("==========")
            for subtipo in formato.SUB_TIPOS:
                print(f"- {subtipo}")

    def comprimir_anuncio(self):
        """
        Método abstracto para compresión de anuncios.

        Raises:
            NotImplementedError: Si el método no está implementado.
        """
        raise NotImplementedError("Método 'comprimir_anuncio' no implementado")

    def redimensionar_anuncio(self):
        """
        Método abstracto para redimensionamiento de anuncios.

        Raises:
            NotImplementedError: Si el método no está implementado.
        """
        raise NotImplementedError("Método 'redimensionar_anuncio' no implementado")


class Video(Anuncio):
    """
    Clase para anuncios de tipo Video.

    Atributos:
        FORMATO (str): Tipo de formato de anuncio.
        SUB_TIPOS (tuple): Subtipos válidos para anuncios de video.
    """

    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")

    def __init__(
        self,
        ancho: int,
        alto: int,
        url_archivo: str,
        url_clic: str,
        sub_tipo: str,
        duracion: int,
    ):
        """
        Inicializa una nueva instancia de Video.

        Args:
            ancho (int): Ancho del anuncio.
            alto (int): Alto del anuncio.
            url_archivo (str): URL del archivo del anuncio.
            url_clic (str): URL de clic del anuncio.
            sub_tipo (str): Subtipo del anuncio.
            duracion (int): Duración del video en segundos.
        """
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)
        self.duracion = self.validar_video(duracion)

    def validar_video(self, parametro: int) -> int:
        """
        Valida que la duración del video sea un entero positivo.

        Args:
            parametro (int): Duración del video a validar.

        Returns:
            int: Duración del video (si es mayor a cero).
            int: 5 (si es menor o igual a cero).
        """
        return parametro if isinstance(parametro, int) and parametro > 0 else 5

    def comprimir_anuncio(self):
        """
        Comprime el anuncio de video.

        Nota:
            Método de compresión aún no implementado.
        """
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        """
        Redimensiona el anuncio de video.

        Nota:
            Método de redimensionamiento aún no implementado.
        """
        print("REDIMENSIONAMIENTO DE VIDEO NO IMPLEMENTADO AÚN")


class Display(Anuncio):
    """
    Clase para anuncios de tipo Display.

    Atributos:
        FORMATO (str): Tipo de formato de anuncio.
        SUB_TIPOS (tuple): Subtipos válidos para anuncios de display.
    """

    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")

    def comprimir_anuncio(self):
        """
        Comprime el anuncio de display.

        Nota:
            Método de compresión aún no implementado.
        """
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        """
        Redimensiona el anuncio de display.

        Nota:
            Método de redimensionamiento aún no implementado.
        """
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")


class Social(Anuncio):
    """
    Clase para anuncios de tipo Social.

    Atributos:
        FORMATO (str): Tipo de formato de anuncio.
        SUB_TIPOS (tuple): Subtipos válidos para anuncios de redes sociales.
    """

    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")

    def comprimir_anuncio(self):
        """
        Comprime el anuncio de redes sociales.

        Nota:
            Método de compresión aún no implementado.
        """
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        """
        Redimensiona el anuncio de redes sociales.

        Nota:
            Método de redimensionamiento aún no implementado.
        """
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")
