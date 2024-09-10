from error import LargoExcedidoError
from anuncio import Social, Display, Video
from datetime import date


class Campaña:
    """
    Representa una campaña publicitaria que contiene una lista de anuncios.

    Atributos:
        nombre (str): Nombre de la campaña.
        fecha_inicio (date): Fecha de inicio de la campaña.
        fecha_termino (date): Fecha de término de la campaña.
        anuncios (list): Lista de anuncios asociados a la campaña.
    """

    def __init__(
        self, nombre: str, fecha_inicio: date, fecha_termino: date, anuncios: list
    ):
        """
        Inicializa una nueva instancia de la campaña.

        Args:
            nombre (str): Nombre de la campaña.
            fecha_inicio (date): Fecha de inicio de la campaña.
            fecha_termino (date): Fecha de término de la campaña.
            anuncios (list): Lista de diccionarios que representan anuncios.

        Raises:
            LargoExcedidoError: Si el nombre de la campaña tiene más de 250 caracteres.
        """
        if len(nombre) > 250:
            raise LargoExcedidoError("El nombre no puede tener más de 250 caracteres.")
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = [self.__instancia_anuncio(anuncio) for anuncio in anuncios]

    def __instancia_anuncio(self, anuncio: dict):
        """
        Crea una instancia de anuncio basado en el tipo especificado en el diccionario.

        Argumentos:
            anuncio (dict): Diccionario con la información del anuncio.

        Retorna:
            Anuncio: Una instancia del tipo de anuncio correspondiente.

        """
        tipo_anuncio = anuncio.get("tipo", "").lower()
        ancho = anuncio.get("ancho", 0)
        alto = anuncio.get("alto", 0)
        url_archivo = anuncio.get("url_archivo", "")
        url_clic = anuncio.get("url_clic", "")
        sub_tipo = anuncio.get("sub_tipo", "")
        duracion = int(anuncio.get("duracion", 0))

        if tipo_anuncio == "video":
            return Video(ancho, alto, url_archivo, url_clic, sub_tipo, duracion)
        elif tipo_anuncio == "social":
            return Social(ancho, alto, url_archivo, url_clic, sub_tipo)
        else:
            return Display(ancho, alto, url_archivo, url_clic, sub_tipo)

    @property
    def nombre(self):
        """Getter de nombre de la campaña
        Retorna:
            str: Nombre
        """
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        """
        Setter de la nombre de la campaña.

        Args:
            nombre (str): Nueva nombre de la campaña.
        """
        self.__nombre = nombre

    @property
    def anuncios(self):
        """Getter de anuncios de la campaña
        Retorna:
            str: anuncios
        """
        return self.__anuncios

    @property
    def fecha_inicio(self):
        """Getter de fecha de inicio de la campaña
        Retorna:
            str: fecha_inicio
        """
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio: date):
        """
        Setter de la fecha de inicio de la campaña.

        Args:
            fecha_inicio (date): Nueva fecha de inicio de la campaña.
        """
        self.__fecha_inicio = fecha_inicio

    @property
    def fecha_termino(self):
        """Getter de fecha de termino de la campaña
        Retorna:
            str: fecha_termino
        """
        return self.__fecha_termino

    @fecha_termino.setter
    def fecha_termino(self, fecha_termino: date):
        """
        Setter de la fecha de término de la campaña.

        Args:
            fecha_termino (date): Nueva fecha de término de la campaña.
        """
        self.__fecha_termino = fecha_termino

    def __str__(self):
        """
        Representación en cadena de la instancia de la campaña.

        Returns:
            str: cadena_texto: Información de la campaña y la cantidad de anuncios por tipo.
        """
        tiposdeanuncio = {"video": 0, "display": 0, "social": 0}
        for anuncio in self.anuncios:
            if anuncio.__class__.__name__ == "Video":
                tiposdeanuncio["video"] += 1
            elif anuncio.__class__.__name__ == "Display":
                tiposdeanuncio["display"] += 1
            elif anuncio.__class__.__name__ == "Social":
                tiposdeanuncio["social"] += 1

        cadena_texto = (
            f"Nombre de la campaña: {self.__nombre}\n"
            f"Anuncios: {tiposdeanuncio['video']} Video, {tiposdeanuncio['display']} Display, {tiposdeanuncio['social']} Social"
        )

        return cadena_texto
