import wget
import os

path = r"C:\Users\Guilherme\Documents\ETL-eptc-main\datasets"


def extract_vitimas():
    try:
        link = "https://dadosabertos.poa.br/dataset/ddc7c320-d52a-469f-831a-921b30feb48c/resource/a46aaaca-8cc1-4082-aa78-ce9f859e2df5/download/cat_vitimas.csv"
        filename = path + '/' + os.path.basename(link)

        if os.path.exists(filename):
            os.remove(filename)

        wget.download(link, filename)
    except:
        pass

def extract_acidentes():
    link = "https://dadosabertos.poa.br/dataset/d6cfbe48-ee1f-450f-87f5-9426f6a09328/resource/b56f8123-716a-4893-9348-23945f1ea1b9/download/cat_acidentes.csv"
    filename = path + '/' + os.path.basename(link)

    if os.path.exists(filename):
        os.remove(filename)

    wget.download(link, filename)

