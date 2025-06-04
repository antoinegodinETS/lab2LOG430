from common.database import init_db
from magasin.services import performances_magasin, generer_rapport_ventes
from logistique.services import approvisionner_magasin, verifier_et_reapprovisionner
from maison_mere.services import mettre_a_jour_produit


if __name__ == "__main__":
    init_db()
    print("✅ Base de données initialisée avec succès.")
