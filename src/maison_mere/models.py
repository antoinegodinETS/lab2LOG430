from sqlalchemy import Column, Integer, String, Float
from common.database import Base

class Vente(Base):
    __tablename__ = "ventes"

    id = Column(Integer, primary_key=True, index=True)
    magasin_id = Column(Integer)
    produit_id = Column(Integer)
    quantite = Column(Integer)
    montant = Column(Float)

    def __repr__(self):
        return f"<Vente(magasin_id={self.magasin_id}, produit_id={self.produit_id}, montant={self.montant})>"
