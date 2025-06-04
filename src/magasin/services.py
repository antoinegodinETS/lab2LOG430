from common.database import SessionLocal
from maison_mere.models import Vente, Produit
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
