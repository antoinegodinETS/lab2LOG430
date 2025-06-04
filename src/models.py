from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, relationship
import datetime

Base = declarative_base()


class Produit(Base):
    __tablename__ = 'produits'
    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False)
    categorie = Column(String, nullable=False)
    prix = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)


class Vente(Base):
    __tablename__ = 'ventes'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    total = Column(Float, nullable=False)
    caisse = Column(Integer, nullable=False)
    annulee = Column(Boolean, default=False)   # <-- AJOUT ICI
    lignes = relationship("VenteLigne", back_populates="vente")


class VenteLigne(Base):
    __tablename__ = 'ventes_lignes'
    id = Column(Integer, primary_key=True)
    vente_id = Column(Integer, ForeignKey('ventes.id'))
    produit_id = Column(Integer, ForeignKey('produits.id'))
    quantite = Column(Integer, nullable=False)
    sous_total = Column(Float, nullable=False)
    vente = relationship("Vente", back_populates="lignes")
    produit = relationship("Produit")
