from sqlalchemy import create_engine, text
from models import CONN

def sqlConnector():
    # Carrega as credenciais do segredo
    host =
    database =
    username =
    password =
    port =

    # Cria a string de conexão para PostgreSQL
    new_con = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"

    # Cria e retorna o engine do SQLAlchemy
    return create_engine(new_con)

def load_data(schema,table, df, pk):
    #logging.basicConfig()
    #logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
    engine = sqlConnector()

    # Define um valor seguro para chunksize considerando os limites do PostgreSQL
    max_params = 65535  # Limite de parâmetros em uma query no PostgreSQL
    chunksize = (max_params // len(df.columns)) - 1

    try:
        # Insere os dados no banco usando pandas to_sql
        df.to_sql(
            name=table,
            index=False,
            schema=schema,
            con=engine,
            if_exists='append',
            method='multi',
            chunksize=chunksize
        )

        print(f'Inserted into {table}')
    except Exception as e:
        print("Error inserting data:", e)

    engine = sqlConnector()
    conn = engine.connect()
    conn.execute(text(f"""
                            WITH cte AS (
                                SELECT {pk}, MAX(inserted_at) AS max_data
                                FROM {schema}.{table}
                                GROUP BY {pk}
                            )
                            DELETE FROM {schema}.{table}
                            WHERE {pk} IN (
                                SELECT {pk}
                                FROM cte
                            )
                            AND inserted_at <> (
                                SELECT max_data
                                FROM cte
                                WHERE cte.{pk} = {table}.{pk}
                            );
                        """))
    conn.commit()
    conn.close()
    print(f'dedudplicated {table}')
    return

