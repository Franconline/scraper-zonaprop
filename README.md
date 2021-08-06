# Web Scraping de página ZonaProp

_Proyecto de web scraping hecho en Python usando Selenium y Pandas como librerias, entre otras._

## Funcionamiento

_El codigo principal se encuentra en el archivo scraper.py , dentro de él se encuentra la clase Scraper_

_ La clase Scraper recibe como primer argumento un link que debe ser, en esta versión, exclusivamente de la página zonaprop.com.ar_

### Modulos

_ scrapear() recolecta los datos de la página especificada y los guarda como atributo del objeto _

_ procesar_datos() crea un archivo excel con los datos procesados. Se le puede especificar un valor máximo de alquiler de los departamentos requeridos, 
es decir, lo que exportará será todos los departamentos que se encuentren por debajo de ese valor_

_ abrir_tabla() abre la tabla hecha en el programa por defecto del sistema operativo para abrir archivos xlxs _

