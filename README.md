# Web Scraping de página ZonaProp

_Proyecto de web scraping hecho en Python usando Selenium y Pandas como librerias, entre otras._

## Funcionamiento

_El codigo principal se encuentra en el archivo scraper.py , dentro de él se encuentra la clase Scraper_

_La clase Scraper recibe como primer argumento un link que debe ser, en esta versión, exclusivamente de la página zonaprop.com.ar_

### Modulos

_scrapear() recolecta los datos de la página especificada y los guarda como atributo del objeto_

_procesar_datos() crea un archivo excel con los datos procesados. Se le puede especificar un valor máximo de alquiler de los departamentos requeridos, 
es decir, lo que exportará será todos los departamentos que se encuentren por debajo de ese valor_

_abrir_tabla() abre la tabla hecha en el programa por defecto del sistema operativo para abrir archivos xlxs_


### Funcionalidad a agregar

_[ ]Poder actualizar una tabla a partir de otra_
_[ ]Que se permita definir si se quiere ordenar la tabla de menor a mayor respecto de los valores_
