from common.database import SessionLocal
from maison_mere.models import Vente, Produit

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