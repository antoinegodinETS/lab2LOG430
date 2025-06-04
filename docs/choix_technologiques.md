# Choix technologiques

## Langage de programmation
**Python 3**
- Simple, rapide à mettre en place
- Excellente lisibilité
- Large communauté et documentation

## ORM (Object-Relational Mapper)
**SQLAlchemy**
- Permet de manipuler la base de données de façon simple et abstraite
- Prise en charge native de SQLite
- Documentation riche, usage courant dans l’industrie et l’éducation

## Base de données
**SQLite (locale)**
- Aucune installation serveur nécessaire, simple fichier local
- Parfait pour un laboratoire, portabilité maximale
- Transactions ACID pour garantir la cohérence des ventes/stocks

## Gestion des dépendances et environnements
- **pip** pour installer les packages Python
- **requirements.txt** pour lister les dépendances

## Conteneurisation
- **Docker**
  - Facilite le déploiement et la portabilité du projet sur toutes plateformes
  - Reproductibilité de l’environnement de développement/test/production

- **docker-compose**
  - Orchestration si besoin de séparer application et base de données

## Tests et qualité
- **pytest** pour les tests unitaires
- **flake8** pour la vérification du style et de la qualité du code Python

## Génération de documentation et UML
- **PlantUML** pour les diagrammes (modèle 4+1)
- **Markdown** pour la documentation et les ADRs

---

## Justification des choix

- **Simplicité** : chaque technologie est reconnue pour sa prise en main rapide et son faible coût d’installation
- **Portabilité** : Docker et SQLite garantissent l’exécution sur tous les environnements sans configuration complexe
- **Évolutivité** : Passage futur à une vraie base SQL (PostgreSQL) ou à une application distribuée facilité par ce stack

