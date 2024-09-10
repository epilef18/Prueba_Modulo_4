from campaña import Campaña
from datetime import date
import logging


campañademo = Campaña(
    "Demo",
    date.today(),
    date.today(),
    [
        {
            "tipo": "video",
            "url_clic": "n/a",
            "url_archivo": "n/a",
            "sub_tipo": "outstream",
            "duracion": "10",
        }
    ],
)

try:
    nombre = input("Ingrese nombre nuevo para la campaña: ")
    campañademo.nombre = nombre

    sub_tipo = input("Ingrese el subtipo del anuncio: ")
    campañademo.anuncios[0].sub_tipo = sub_tipo

except Exception as e:
    logging.error(f"{e}")
    print("Error registrado en error.log")


logging.basicConfig(filename="error.log", level=logging.ERROR)
