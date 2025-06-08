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

def generer_performances_magasin():
    return {
        "chiffre_affaires": {
            1: 12345,
            2: 11200,
            3: 8900,
            4: 15000,
            5: 9700,
        },
        "ruptures_stock": [
            {"produit_id": 1, "nom": "Produit A", "magasin_id": 2, "quantite": 2},
            {"produit_id": 2, "nom": "Produit B", "magasin_id": 5, "quantite": 1},
        ],
        "surstock": [
            {"produit_id": 3, "nom": "Produit C", "magasin_id": 1, "quantite": 120},
        ],
        "tendances_hebdo": [
            {"semaine": "Semaine 22", "ventes": [1500, 1800, 2000, 2200, 2100]},
        ]
    }


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
