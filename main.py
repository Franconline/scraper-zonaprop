from scraper import Scraper

VALOR_MAXIMO = 16000

URL_BASE = "https://www.zonaprop.com.ar/departamentos-alquiler-la-plata.html"
URL_MODIF = "-pagina-numero.html"
# defino una sola url_modfi en vez de una list, y con un for range hago este replace de abajo, reemplazando por un str(index)

scraper = Scraper(URL_BASE)
scraper.scrapear()
scraper.procesar_datos(VALOR_MAXIMO, True)
nombre_tabla_original = scraper.table_name


# La primera vez que actualizo la tabla lo hago con la tabla base, ya dsp lo hago con tabla_concatenada
nueva_url = URL_BASE.replace(".html", URL_MODIF.replace("numero", "2"))
nuevo_scraper = Scraper(nueva_url)
nuevo_scraper.scrapear()
nuevo_scraper.actualizar_tabla(nombre_tabla_original, VALOR_MAXIMO)


for index in range(3, 27):
    nueva_url = URL_BASE.replace(".html", URL_MODIF.replace("numero", str(index)))
    nuevo_scraper = Scraper(nueva_url)
    nuevo_scraper.scrapear()
    try:
        nuevo_scraper.actualizar_tabla("tabla_concatenada.xlsx", VALOR_MAXIMO)
    except:
        print(f"Error en link ->{nueva_url}")

