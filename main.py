from scraper import Scraper

URL = "https://www.zonaprop.com.ar/departamentos-alquiler-q-la-plata.html"

scraper = Scraper(URL)
scraper.scrapear()
scraper.procesar_datos(18000, True)
scraper.abrir_tabla()
