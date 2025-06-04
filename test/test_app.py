from db import init_db
from repository import ajouter_produit, lister_produits, enregistrer_vente, annuler_vente, lister_ventes
import sys
import os
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '../src')))


def setup_module(module):
    # Nettoyer la base de données avant chaque module de tests
    if os.path.exists("pos.db"):
        os.remove("pos.db")
    init_db()


def test_ajout_produit():
    ajouter_produit("TestProduit", "TestCat", 2.5, 10)
    produits = lister_produits()
    assert any(p.nom == "TestProduit" for p in produits)


def test_enregistrer_vente_et_stock():
    ajouter_produit("Pomme", "Fruit", 1.0, 10)
    produits = lister_produits()
    produit_pomme = next(p for p in produits if p.nom == "Pomme")
    ok, msg = enregistrer_vente([(produit_pomme.id, 3)], caisse_num=1)
    assert ok
    # Vérifie que le stock a décrémenté
    produits = lister_produits()
    pomme = next(p for p in produits if p.nom == "Pomme")
    assert pomme.stock == 7


def test_annuler_vente():
    ajouter_produit("Baguette", "Boulangerie", 2.0, 5)
    produit = next(p for p in lister_produits() if p.nom == "Baguette")
    ok, msg = enregistrer_vente([(produit.id, 2)], caisse_num=1)
    ventes = lister_ventes()
    vente_id = ventes[-1].id
    ok, msg = annuler_vente(vente_id)
    assert ok
    # Vérifie que la vente est annulée
    ventes = lister_ventes()
    vente = next(v for v in ventes if v.id == vente_id)
    assert vente.annulee
    # Vérifie que le stock a été remis à jour
    produit = next(p for p in lister_produits() if p.nom == "Baguette")
    assert produit.stock == 5
