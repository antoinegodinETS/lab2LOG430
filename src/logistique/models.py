from sqlalchemy import Column, Integer, String
from common.database import Base

class StockLogistique(Base):
    __tablename__ = "stock_logistique"

    id = Column(Integer, primary_key=True, index=True)
    produit_id = Column(Integer)
    quantite = Column(Integer)

    def __repr__(self):
        return f"<StockLogistique(produit_id={self.produit_id}, quantite={self.quantite})>"
