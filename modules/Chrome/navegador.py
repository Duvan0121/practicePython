from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from modules.evidences.evidence import evidence

fila = int(input('Que fila del excel vamos a usar? '))
driver = webdriver.Chrome()

def abrirNavegador():
        try:
                global driver
                driver.maximize_window()
                driver.get('https://www.facebook.com/')
                evidence("Entre a la página indicada")
                return driver
        except Exception as e:
                print("No pude abrir el navegador")


def digitar(elemento,tiempo,texto):
        try:
                global driver
                validador = WebDriverWait(driver,tiempo).until(EC.element_to_be_clickable((By.XPATH,elemento)))
                try:
                        validador.send_keys(str(texto))
                except Exception as e:
                        print("No pude ingresar la informacion")
        except Exception as e:
                print("El elemento no fue interactuable en el tiempo esperado")

def clickear(elemento,tiempo):
        try:
                global driver
                validador = WebDriverWait(driver,tiempo).until(EC.element_to_be_clickable((By.XPATH,elemento)))
                validador.click()
        except Exception as e:
                print("El boton no es clickeable")
