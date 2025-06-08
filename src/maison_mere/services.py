from sqlalchemy.orm import Session
from common.database import SessionLocal
from magasin.models import Magasin, Produit, StockMagasin
from maison_mere.models import Vente
from sqlalchemy import func

def generer_rapport_ventes():
    session: Session = SessionLocal()
    
    # 1. Ventes par magasin
    ventes_par_magasin = session.query(
        Magasin.nom,
        func.sum(Vente.montant).label("total_ventes")
    ).join(Magasin, Magasin.id == Vente.magasin_id)\
     .group_by(Magasin.nom).all()

    # 2. Produits les plus vendus (quantité)
    produits_vendus = session.query(
        Produit.nom,
        func.sum(Vente.quantite).label("quantite_totale")
    ).join(Produit, Produit.id == Vente.produit_id)\
     .group_by(Produit.nom).order_by(func.sum(Vente.quantite).desc()).limit(5).all()

    # 3. Stock restant
    stock_restants = session.query(
        Magasin.nom.label("magasin"),
        Produit.nom.label("produit"),
        StockMagasin.quantite
    ).join(Produit, Produit.id == StockMagasin.produit_id)\
     .join(Magasin, Magasin.id == StockMagasin.magasin_id).all()

    session.close()

    return {
        "ventes_par_magasin": ventes_par_magasin,
        "produits_vendus": produits_vendus,
        "stock_restants": stock_restants
    }

def mettre_a_jour_produit(produit_id, nouvelles_infos):
    session = SessionLocal()
    produit = session.query(Produit).filter(Produit.id == produit_id).first()
    if not produit:
        return False
    for cle, val in nouvelles_infos.items():
        setattr(produit, cle, val)
    session.commit()
    session.close()
    return True