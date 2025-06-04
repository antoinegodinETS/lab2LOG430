from logistique.models import StockLogistique
from common.database import SessionLocal


def approvisionner_magasin(produit_id, quantite):
    session = SessionLocal()
    stock = session.query(StockLogistique).filter(StockLogistique.produit_id == produit_id).first()
    if stock:
        stock.quantite += quantite
        session.commit()
    session.close()
    return True

def verifier_et_reapprovisionner():
    session = SessionLocal()
    stocks = session.query(StockLogistique).all()
    alertes = []
    for stock in stocks:
        if stock.quantite < stock.seuil_minimum:
            alertes.append({
                "produit_id": stock.produit_id,
                "stock_actuel": stock.quantite,
                "seuil_minimum": stock.seuil_minimum,
                "action": "Reapprovisionner"
            })
    session.close()
    return alertes
