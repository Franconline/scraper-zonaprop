from numpy import mod
from scraper import Scraper

URL_BASE = "https://www.zonaprop.com.ar/departamentos-alquiler-q-la-plata.html"
modificaciones_url = ["-pagina-2-q","-pagina-3-q", "-pagina-4-q", "-pagina-5-q", "-pagina-6-q", "-pagina-7-q"]

scraper = Scraper(URL_BASE)
scraper.scrapear()
scraper.procesar_datos(18000, True)
nombre_tabla_original = scraper.table_name



for url in modificaciones_url:
    # Crear objeto, y hacer que actualice la tabla original(actualizar es agregarle los datos de esa pagina) 
    nueva_url = URL_BASE.replace("-q", url)
    nuevo_scraper = Scraper(nueva_url)
    nuevo_scraper.scrapear()
    nuevo_scraper.actualizar_tabla(nombre_tabla_original)
