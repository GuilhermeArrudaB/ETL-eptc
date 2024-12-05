import time
from selenium import webdriver


def extract_vitimas():
    navegador = webdriver.Chrome()

    navegador.get("https://dadosabertos.poa.br/dataset/acidentes-de-transito-vitimas")

    cl = "resource-url-analytics.btn.btn-primary"

    btn_download = navegador.find_elements("css selector", f".{cl.replace(' ', '.')}")

    btn_download[1].click()

    time.sleep(10)


def extract_acidentes():
    navegador = webdriver.Chrome()

    navegador.get("https://dadosabertos.poa.br/dataset/acidentes-de-transito-acidentes")

    cl = "resource-url-analytics.btn.btn-primary"

    btn_download = navegador.find_elements("css selector", f".{cl.replace(' ', '.')}")

    btn_download[1].click()

    time.sleep(20)


