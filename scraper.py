from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
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
        self.table_name = f"tabla-{actual_time}.xlsx"

    def scrapear(self):
        """ El método scrapear() no requiere argumentos. Recolecta todos los datos de la página especificada en el constructor"""
        driver = self.__iniciar_opciones()
        driver.get(self.url)
        driver.maximize_window() # se maximiza la ventana pq hay veces que el boton no aparece x tener la ventana no maximizada
        time.sleep(3)
        self.__cerrar_boton(driver)
        self.data = self.__recolectar_datos(driver)
        driver.quit() # ya no necesito el driver, tengo la data guardada

    def __iniciar_opciones(self):
        options = Options()
        userAgent = "Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36"
        options.add_argument(f'--user-agent={userAgent}')
        driver = webdriver.Chrome()
        return driver
    

    def __cerrar_boton(self, driver):
        try:
          driver.find_element_by_class_name("mdl-close-btn").click() # para cerrar un cartel de error que sale
        except:
            print("No pude cerrar boton")


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

    def __crear_dataframe(self):
        df = pd.DataFrame(self.data, columns=[key for key in self.data])
        return df
    
    def __valor_maximo_tabla(self, valor_maximo, df):
        df = df[df.Precios <= valor_maximo]
        return df
    
    def __ordenar_por_precios(self, df):
        df.sort_values(by=["Precios"], inplace = True)
        return df

    def procesar_datos(self, valor_maximo = 0, orden_tabla = False):
        """ procesar_datos() usa los datos recolectados en el método scrapear() y los convierte a excel de manera ordenada y con un precio menor al requerido
        Si ningun precio es especificado, toma todos los datos que encuentre"""
        df = self.__crear_dataframe()
        if valor_maximo != 0:
            df = self.__valor_maximo_tabla(valor_maximo, df)
        if orden_tabla:
            df = self.__ordenar_por_precios(df)
        df.to_excel(self.table_name, index=False)
        print(f"Tabla hecha, nombre en directorio: {self.table_name}")
        
    def abrir_tabla(self):
        os.startfile(self.table_name)

    
    def actualizar_tabla(self, nombre_tabla_base, valor_maximo = 0):
        """ Recibe como argumento el nombre de la tabla actualizar. Si la tabla existe y tengo datos procesados, mergea los datos."""
        # Primero debo crear el dataframe de la tabla actual, y luego lo concateno con el existente
        # Debere leer el excel del dataframe base, para tenerlo en memoria y manipularlo
        if os.path.isfile(nombre_tabla_base):
            # Leer dataframe de la tabla original
            df_base = pd.read_excel(nombre_tabla_base)
            # Crear dataframe de tabla actual
            nueva_df = self.__crear_dataframe()
            if valor_maximo != 0:
                nueva_df = self.__valor_maximo_tabla(valor_maximo, nueva_df)
            # Concatenar
            tabla_concatenada = pd.concat([df_base, nueva_df])
            tabla_concatenada = self.__ordenar_por_precios(tabla_concatenada)
            tabla_concatenada.to_excel("tabla_concatenada.xlsx", index=False)
            print("Tabla concatenada")
        else:
            print("Tabla no encontrada")