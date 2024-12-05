from etl.extract import extract_acidentes, extract_vitimas
from etl.transform import transform_acidentes, transform_vitimas
from etl.load import load_data
import logging


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    logging.info('Downloading vitimas file')
    extract_vitimas()

    logging.info('Downloading acidentes file')
    extract_acidentes()

    logging.info('Files downloaded')

    logging.info('Transforming vitimas data')
    df_vitimas = transform_vitimas()

    logging.info('Transforming acidentes data')
    df_acidentes = transform_acidentes()

    logging.info('Data transformed')

    logging.info('Loading data')
    load_data('public', 'vitimas',df_vitimas, 'idacidente')
    load_data('public', 'acidentes',df_acidentes, 'idacidente')

    logging.info('Data loaded')

    logging.info('ETL completed')

main()