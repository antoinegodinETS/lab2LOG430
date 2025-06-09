from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import MetaData


engine = create_engine("postgresql+psycopg://lab2user:password@localhost/lab2db", connect_args={"options": "-csearch_path=lab2_schema"})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base(metadata=MetaData(schema="lab2_schema"))


def init_db():
    with engine.connect() as conn:
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS lab2_schema"))
    
    
    from magasin.models import Magasin, StockMagasin, Produit
    from logistique.models import StockLogistique, DemandeApprovisionnement
    from maison_mere.models import Vente
    
    Base.metadata.create_all(bind=engine)
