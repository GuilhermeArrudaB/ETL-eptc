from etl.extract import extract_acidentes, extract_vitimas, path
import pandas as pd
import csv
from datetime import datetime


def transform_acidentes():
    df = pd.read_table(path + '/' + 'cat_acidentes.csv', sep=';')
    # Adicionando registro de inserção no banco
    df['inserted_at'] = datetime.now()

    # Alterando o nome de algumas colunas para deixar mais dinâmico
    df = df.rename(columns={
        "feridos_gr": "feridos_graves",
        "cont_vit": "contem_vitimas",
        "queda_arr": "queda_em_arroio",
    })

    return df


def transform_vitimas():
    df = pd.read_table(path + '/' + 'cat_vitimas.csv', sep=';')
    # Adicionando registro de inserção no banco
    df['inserted_at'] = datetime.now()

    # Alterando o nome de algumas colunas para deixar mais dinâmico
    df = df.rename(columns={
        "sit_vitima": "situacao_vitima",
        "fx_et": "faixa_etaria",
        "dia_sem": "dia_semana",
        "periododia": "periodo_do_dia"
    })

    return df

