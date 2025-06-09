# Système de gestion de caisse POS (Python/FastAPI/PostgreSQL)

Une application web Python pour la gestion de caisse d’un magasin local, avec persistance des données via PostgreSQL et interface moderne basée sur FastAPI.

---

## Démarrage rapide

### **Installer les dépendances :**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### **Lancer l’application localement :**
```bash
uvicorn src.interface:app --host 0.0.0.0 --port 8000 --reload
```

### **Lancer avec Docker :**
```bash
docker-compose up --build
```

---

## Structure du projet

```
├── .github/
│   └── workflows/         # Workflows GitHub Actions (CI/CD)
│       └── python-app.yml
├── docs/                  # Documentation, ADRs, diagrammes UML
│   ├── analyse_besoins.md
│   ├── choix_technologiques.md
│   └── ADR/
│       ├── ADR_Choix_Base_Donnees.md
│       └── ADR_Choix_Plateforme.md
├── src/                   # Code source principal de l’application
│   ├── interface.py       # Interface FastAPI
│   ├── models/            # Modèles SQLAlchemy
│   ├── services/          # Logique métier
│   ├── common/            # Configuration et utilitaires
│   └── database.py        # Configuration de la base de données
├── test/                  # Tests unitaires (pytest)
│   └── test_app.py
├── .gitignore             # Fichiers/dossiers à ignorer par git
├── docker-compose.yml     # Orchestration Docker Compose
├── Dockerfile             # Image Docker de l’application
├── LICENSE                # Licence MIT
├── README.md              # Documentation du projet
├── requirements.txt       # Dépendances Python
```

---

## Fonctionnalités

- Ajout, consultation et gestion des produits
- Enregistrement et annulation de ventes
- Gestion du stock en temps réel
- Historique des ventes
- Interface web moderne avec FastAPI
- Persistance via PostgreSQL
- Prise en charge multi-caisses
- Déploiement avec Docker et Docker Compose

---

## CI/CD (Intégration et Déploiement Continus)

Ce projet utilise **GitHub Actions** pour automatiser les étapes de CI/CD.  
Le workflow se trouve dans `.github/workflows/python-app.yml`.

### Fonctionnement du pipeline CI/CD

- **Déclenchement** : À chaque push ou pull request sur la branche principale
- **Étapes principales** :
  - Installation des dépendances (`pip install -r requirements.txt`)
  - Exécution des tests unitaires (pytest)
  - Initialisation de la base de données PostgreSQL
  - Build et publication de l’image Docker (si les tests passent)

---

## Choix techniques

- **Python 3** : Rapidité de développement, lisibilité, large communauté
- **FastAPI** : Framework moderne pour créer des API web rapides et performantes
- **SQLAlchemy** : ORM pour simplifier la gestion de la base de données
- **PostgreSQL** : Base de données robuste et adaptée aux environnements multi-utilisateurs
- **pytest** : Tests unitaires
- **Docker & Docker Compose** : Portabilité et reproductibilité de l’environnement
- **GitHub Actions** : CI/CD intégré et automatisé

---

## Licence

Ce projet est sous licence MIT. Voir [LICENSE](LICENSE).