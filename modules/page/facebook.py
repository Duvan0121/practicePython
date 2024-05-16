from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from modules.Chrome.navegador import *
from modules.evidences.evidence import evidence
from modules.data.manejoData import obtener_valor_en_celda



driver = abrirNavegador()

email = "//input[@id='email']"
password = "//input[@id='pass']"
btnOk = "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button"



emailValor = obtener_valor_en_celda('email',fila)
passValor = obtener_valor_en_celda('password',fila)

digitar(email,10,emailValor)
evidence("ingreso el correo")
digitar(password,10,passValor)
evidence("ingreso la clave")
clickear(btnOk,10)
time.sleep(5)
evidence("Doy click en iniciar sesion")
