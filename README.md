# Prueba Programación Avanzada en Python

## Descripcion del proyecto

En este proyecto se desarrolla una API para gestionar campañas publicitarias multiplataforma tanto para desarrolladores front-end como para clientes.

## Funciones

- Crea y gestiona campañas publicitarias.
- Crea y modifica distintos tipos de Anuncios.
- Informa al usuario de errores al ingresar parametros para instanciar una campaña.
- Almacena los errores en un log

## Estructura

El proyecto sigue una logica de programacion orientada a objetos, por lo que su estructura se basa en distintas clases, además de una interfaz de usuario, un script para manejo de errores y un log donde se guardan los errores ocurridos.

## Diagrama de Clases

![Diagrama de Clases](/Diagramadeclases.png)

## Clases

**Anuncio**: Clase padre de los distintos tipos de anuncios, los cuales derivan de Anuncio.(Video, Display, Social)
**Clase Campaña**: Clase donde se almacenan y administran los distintos anuncios

Manejo de errores:
Clase:
**Error**: Subclase de Exception
**LargoExcedidoError**: Cuando el nombre de una campaña supera los 250 caracteres.
**SubTipoInvalidoError**: Cuando el subtipo ingresado en demo.py no pertenece a los sub tipos de cada clase derivada de Anuncio.

## Interfaz de usuario

**demo.py**: Instancia una campaña publicitaria, solicitando su nombre y sub tipo al usuario.

## Log

**error.log**: Guardará los errores llamados por Exception.

## Instrucciones para ejecutar demo

**Correr el script demo.py en la terminal**

## Autor

Felipe Villarroel

## Entregables

- anuncio.py
- campaña.py
- demo.py
- error.py
- Diagramadeclases.png
- README.md
- error.log
