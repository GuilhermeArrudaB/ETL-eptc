from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, DateTime, Time
from sqlalchemy.orm import sessionmaker, declarative_base

CONN = "sqlite:///database_eptc.db"

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Acidente(Base):
    __tablename__ = "acidentes"
    id_insert = Column(Integer, primary_key=True, autoincrement=True)
    idacidente = Column(Integer)

    data_extracao = Column(DateTime)
    predial1 = Column(String(255))
    queda_em_arroio = Column(Integer)
    data = Column(DateTime)
    feridos = Column(Integer)
    feridos_graves = Column(Integer)
    mortes = Column(Integer)
    morte_post = Column(Integer)
    fatais = Column(Integer)
    auto = Column(Integer)
    taxi = Column(Integer)
    lotacao = Column(Integer)
    onibus_urb = Column(Integer)
    onibus_met = Column(Integer)
    onibus_int = Column(Integer)
    caminhao = Column(Integer)
    moto = Column(Integer)
    carroca = Column(Integer)
    bicicleta = Column(Integer)
    outro = Column(Integer)
    contem_vitimas = Column(Integer)
    ups = Column(Integer)
    patinete = Column(Integer)
    longitude = Column(Float)
    latitude = Column(Float)
    log1 = Column(String(255))
    log2 = Column(String(255))
    tipo_acid = Column(String(100))
    dia_sem = Column(String(100))
    hora = Column(Time)
    noite_dia = Column(String(100))
    regiao = Column(String(100))
    consorcio = Column(String(100))
    inserted_at = Column(DateTime)


class Vitima(Base):
    __tablename__ = "vitimas"
    id_insert = Column(Integer, primary_key=True, autoincrement=True)
    idacidente = Column(Integer)

    data_extracao = Column(DateTime)
    longitude = Column(Float)
    latitude = Column(Float)
    data = Column(DateTime)
    hora = Column(Time)
    idade = Column(Integer)
    sexo = Column(String(50))
    situacao_vitima = Column(String(50))
    log1 = Column(String(255))
    log2 = Column(String(255))
    predial1 = Column(String(255))
    regiao = Column(String(100))
    tipo_acid = Column(String(100))
    auto = Column(Integer)
    taxi = Column(Integer)
    onibus_urb = Column(Integer)
    onibus_met = Column(Integer)
    onibus_int = Column(Integer)
    caminhao = Column(Integer)
    moto = Column(Integer)
    carroca = Column(Integer)
    bicicleta = Column(Integer)
    outro = Column(Integer)
    lotacao = Column(Integer)
    dia_semana = Column(String(50))
    periodo_do_dia = Column(String(50))
    faixa_etaria = Column(String(50))
    tipo_veic = Column(String(100))
    consorcio = Column(String(255))
    inserted_at = Column(DateTime)


Base.metadata.create_all(engine)
