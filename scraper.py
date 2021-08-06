from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import time
import pandas as pd
import datetime as dt
import os


class Scraper:

    def __init__(self, url):
        """ Recibe como argumento el url de la página a scrapear. Solo valido para ZonaProp"""
        self.url = url
        dia_actual = dt.datetime.now().strftime("%d")
        mes_actual = dt.datetime.now().strftime("%m")
        anio_actual = dt.datetime.now().strftime("%Y")
        hora_actual = dt.datetime.now().strftime("%H") + dt.datetime.now().strftime("%M") + dt.datetime.now().strftime("%S")
        actual_time = f"{dia_actual}-{mes_actual}-{anio_actual}-{hora_actual}"
        self.table_name = actual_time

    def scrapear(self):
        """ El método scrapear() no requiere argumentos. Recolecta todos los datos de la página especificada en el constructor"""
        driver = self.__iniciar_opciones()
        driver.get(self.url)
        time.sleep(3)
        self.__cerrar_boton(driver)
        self.data = self.__recolectar_datos(driver)
        driver.quit() # ya no necesito el driver, tengo la data guardada

    def __iniciar_opciones(self):
        options = Options()
        ua = UserAgent()
        userAgent = ua.random
        options.add_argument(f'--user-agent={userAgent}')
        driver = webdriver.Chrome(options=options)
        return driver
    

    def __cerrar_boton(self, driver):
        try:
          driver.find_element_by_class_name("mdl-close-btn").click() # para cerrar un cartel de error que sale
        except:
            pass


    def __recolectar_datos(self, driver):
        main = driver.find_element_by_id("main-list-container")
        precios = main.find_elements(By.CLASS_NAME, "firstPrice")
        titulos = main.find_elements(By.CLASS_NAME, "postingCardTitle")
        direcciones = main.find_elements(By.CLASS_NAME, "postingCardLocationTitle")
        elems = main.find_elements(By.CLASS_NAME, "postingCardTitle")
        links = [elem.find_element(By.TAG_NAME, "a").get_attribute("href") for index, elem in enumerate(elems) if index < 21] # esto ya está en string, es una lista de strings

        data = {
            "Titulos" : [title.text for title in titulos],
            "Precios" : [price.text for price in precios],
            "Direcciones" : [direc.text for direc in direcciones],
            "Links" : links,
        }

        for index, prec in enumerate(data["Precios"]):
            data["Precios"][index] = int(float(prec.split(" ")[1])) * 1000

        return data

    def procesar_datos(self, valor_maximo = 0):
        """ procesar_datos() usa los datos recolectados en el método scrapear() y los convierte a excel de manera ordenada y con un precio menor al requerido
        Si ningun precio es especificado, toma todos los datos que encuentre"""
        df = pd.DataFrame(self.data, columns=[key for key in self.data])
        # Deberia checkear si lo que quiero es insertar en una tabla
        # Por ahi puedo hacer otro método que sea insertar_datos y que reciba como argumento el nombre de la tabla, y que el nombre de la tabla
        # sea un atributo del objeto, y tmb al llamar al objeto devuelta eso, el metodo __str__
        if(valor_maximo != 0):
            df = df[df.Precios < 18000]
        df.to_excel(f"tabla-{self.table_name}.xlsx", index=False)
        print(f"Tabla hecha, nombre en directorio: {self.table_name}")
        
    def abrir_tabla(self):
        os.startfile(f"tabla-{self.table_name}.xlsx")