# reset_db.py
from common.database import Base, engine
from magasin.models import Magasin, StockMagasin
from logistique.models import StockLogistique
from maison_mere.models import Vente

print("Suppression et création des tables...")
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
print("Base de données réinitialisée.")
