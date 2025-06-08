from common.database import init_db
from magasin import models as magasin_models
from maison_mere import models as maison_models
from logistique import models as logistique_models



if __name__ == "__main__":
    init_db()
    print("✅ Base de données initialisée avec succès.")
