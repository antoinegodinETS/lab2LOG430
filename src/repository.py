from db import SessionLocal
from models import Produit, Vente, VenteLigne
import datetime


def enregistrer_vente(articles, caisse_num):
    """
    articles = liste de tuples (produit_id, quantite)
    caisse_num = numéro de caisse
    """
    session = SessionLocal()
    total = 0
    vente = Vente(date=datetime.datetime.utcnow(), caisse=caisse_num, total=0)
    session.add(vente)
    session.flush()  # Pour avoir l’ID de la vente

    for produit_id, quantite in articles:
        produit = session.query(Produit).get(produit_id)
        # On récupère le nom maintenant pour l’utiliser en cas d’erreur
        produit_nom = produit.nom if produit else 'Produit inconnu'
        if not produit or produit.stock < quantite:
            session.rollback()
            session.close()
            return False, f"Stock insuffisant pour {produit_nom}"
        sous_total = produit.prix * quantite
        total += sous_total
        produit.stock -= quantite
        ligne = VenteLigne(
            vente_id=vente.id,
            produit_id=produit.id,
            quantite=quantite,
            sous_total=sous_total)
        session.add(ligne)

    vente.total = total
    session.commit()
    session.close()
    return True, f"Vente enregistrée, total: {total:.2f} $"


def ajouter_produit(nom, categorie, prix, stock):
    session = SessionLocal()
    produit = Produit(nom=nom, categorie=categorie, prix=prix, stock=stock)
    session.add(produit)
    session.commit()
    session.close()


def lister_ventes():
    session = SessionLocal()
    ventes = session.query(Vente).all()
    session.close()
    return ventes


def annuler_vente(vente_id):
    session = SessionLocal()
    vente = session.query(Vente).get(vente_id)
    if not vente:
        session.close()
        return False, "Vente non trouvée."
    if vente.annulee:
        session.close()
        return False, "Vente déjà annulée."
    # Remettre en stock chaque produit
    for ligne in vente.lignes:
        produit = session.query(Produit).get(ligne.produit_id)
        produit.stock += ligne.quantite
    vente.annulee = True
    session.commit()
    session.close()
    return True, f"Vente {vente_id} annulée et stock remis à jour."


def lister_produits():
    session = SessionLocal()
    produits = session.query(Produit).all()
    session.close()
    return produits
