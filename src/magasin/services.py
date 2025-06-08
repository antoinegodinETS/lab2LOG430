from common.database import SessionLocal
from magasin.models import Produit, StockMagasin
from maison_mere.models import Vente
from sqlalchemy.orm import joinedload
from sqlalchemy import func

def performances_magasin():
    session = SessionLocal()
    stats = session.query(
        Vente.magasin_id,
        func.sum(Vente.quantite).label("total_ventes")
    ).group_by(Vente.magasin_id).all()
    session.close()
    return [{"magasin_id": r[0], "total_ventes": r[1]} for r in stats]

def generer_rapport_ventes():
    session = SessionLocal()
    ventes = session.query(Vente).options(joinedload(Vente.produit)).all()
    rapport = []
    for vente in ventes:
        rapport.append({
            "produit": vente.produit.nom,
            "quantite": vente.quantite,
            "date": vente.date_vente
        })
    session.close()
    return rapport


def consulter_stock_magasin(magasin_id: int):
    session = SessionLocal()
    stock = (
        session.query(StockMagasin, Produit)
        .join(Produit, StockMagasin.produit_id == Produit.id)
        .filter(StockMagasin.magasin_id == magasin_id)
        .all()
    )
    session.close()

    stock_info = [
        {
            "produit_id": produit.id,
            "nom": produit.nom,
            "quantite": stock_entry.quantite
        }
        for stock_entry, produit in stock
    ]
    return stock_info
