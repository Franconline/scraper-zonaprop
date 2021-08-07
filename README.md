# Web Scraping de página ZonaProp

_Proyecto de web scraping hecho en Python usando Selenium y Pandas como librerias, entre otras._

## Funcionamiento

_El codigo principal se encuentra en el archivo scraper.py , dentro de él se encuentra la clase Scraper_

_La clase Scraper recibe como primer argumento un link que debe ser, en esta versión, exclusivamente de la página zonaprop.com.ar_

_Cuando se llama al método principal que es scrapear() se abre navegador chromium necesario para acceder al HTML de la página, ya que de lo contrario
la página detecta al bot_

_Así y todo la página detecta al bot y se muestra en pantalla un cartel de error, que al cabo de 3seg de espera, el programa cierra automáticamente_

_Luego de recolectar lo necesario el programa se cierra y los datos ya están procesados dentro del objeto_


### Modulos

_scrapear() recolecta los datos de la página especificada y los guarda como atributo del objeto_

_procesar_datos() crea un archivo excel con los datos procesados. Se le puede especificar un valor máximo de alquiler de los departamentos requeridos, 
es decir, lo que exportará será todos los departamentos que se encuentren por debajo de ese valor_

_abrir_tabla() abre la tabla hecha en el programa por defecto del sistema operativo para abrir archivos xlxs_


### Funcionalidad a agregar

- [X] Poder actualizar una tabla a partir de otra
- [X] Que se permita definir si se quiere ordenar la tabla de menor a mayor respecto de los valores
