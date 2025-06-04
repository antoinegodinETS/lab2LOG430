# Système de caisse POS (Python/SQLite)

Une application console Python pour la gestion de caisse d’un magasin local, avec persistance des données via SQLite et interface simple.

---

## Démarrage rapide

**Installer les dépendances :**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Lancer l’application :**
```bash
python src/main.py
```

**(Optionnel) Lancer avec Docker :**
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
│   ├── db.py
│   ├── main.py
│   ├── models.py
│   └── repository.py
├── test/                  # Tests unitaires (pytest)
│   └── test_app.py
├── .gitignore             # Fichiers/dossiers à ignorer par git
├── docker-compose.yml     # Orchestration Docker Compose
├── Dockerfile             # Image Docker de l’application
├── LICENSE                # Licence MIT
├── pos.db                 # Base de données SQLite (générée à l’exécution)
├── README.md              # Documentation du projet
├── requirements.txt       # Dépendances Python
```

---

## Fonctionnalités

- Ajout, consultation et gestion des produits
- Enregistrement et annulation de ventes
- Gestion du stock en temps réel
- Historique des ventes
- Interface console simple et claire
- Persistance locale via SQLite
- Prise en charge multi-caisses

---

## CI/CD (Intégration et Déploiement Continus)

Ce projet utilise **GitHub Actions** pour automatiser les étapes de CI/CD.  
Le workflow se trouve dans `.github/workflows/python-app.yml`.

### Fonctionnement du pipeline CI/CD

- **Déclenchement** : À chaque push ou pull request sur la branche principale
- **Étapes principales** :
  - Installation des dépendances (`pip install -r requirements.txt`)
  - Exécution des tests unitaires (pytest)
  - Build et publication de l’image Docker (si les tests passent)

---

## Choix techniques

- **Python 3** : Rapidité de développement, lisibilité, large communauté
- **SQLAlchemy** : ORM pour simplifier la gestion de la base de données
- **SQLite** : Base de données locale, simple et portable
- **pytest** : Tests unitaires
- **Docker & Docker Compose** : Portabilité et reproductibilité de l’environnement
- **GitHub Actions** : CI/CD intégré et automatisé

---

## Licence

Ce projet est sous licence MIT. Voir [LICENSE](LICENSE).