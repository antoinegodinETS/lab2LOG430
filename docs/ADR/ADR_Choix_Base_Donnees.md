# ADR – Choix du mécanisme de base de données

## Statut
Décision prise – 21 mai 2025

## Contexte
Le système à développer est une application de caisse (POS) locale destinée à un petit magasin de quartier.  
L’application doit être simple, portable et rapide à déployer/tester pour un contexte de laboratoire.

Plusieurs options de base de données existent :
- **SQL local (ex: SQLite)**
- **SQL client/serveur (ex: PostgreSQL)**
- **NoSQL (ex: MongoDB, local ou distant)**

## Décision
Nous avons choisi **SQLite**, en configuration **locale**, comme mécanisme de base de données.

### Raisons principales :
- **Simplicité** : Pas besoin d’installer/configurer un serveur. Un seul fichier local à manipuler.
- **Portabilité** : Fonctionne partout, facilement intégré dans un conteneur Docker. Aucun prérequis logiciel lourd.
- **Localité** : Toute la base de données reste sur la même machine que l’application, ce qui simplifie le développement, la gestion et le déploiement, particulièrement pour un laboratoire ou une démonstration.
- **Intégration** : Support natif ou via ORM dans tous les langages courants (Python, Java, Node.js, etc.).
- **Fiabilité** : Transactions ACID, parfaite pour garantir la cohérence des ventes/stock.
- **Adapté à la charge** : Suffisant pour un magasin local avec peu de concurrence.

Nous avons écarté :
- **PostgreSQL/MySQL** : Trop lourd pour un contexte local de laboratoire ; inutilement complexe pour une seule machine.
- **NoSQL** : Moins naturel pour des opérations transactionnelles classiques (ventes, stocks) et moins intuitif pour un modèle de données tabulaire.
- **Bases de données distantes ou en mode client/serveur** : Surdimensionné, ajoute de la complexité réseau inutile dans le contexte local du laboratoire.

## Conséquences
- Le schéma de la base sera relationnel (tables : Produits, Ventes, Utilisateurs…).
- Les accès se feront via un ORM (ex : SQLAlchemy).
- Le projet sera facile à cloner et exécuter (rien à installer côté BDD).
- Si évolution future : Facile de migrer le schéma vers une BDD plus puissante (PostgreSQL) si besoin.

## Alternatives envisagées mais rejetées
- **MongoDB** : Non adapté au besoin transactionnel ; surdimensionné pour ce cas d’usage.
- **MySQL/PostgreSQL** : Plus complexe à installer/maintenir pour ce laboratoire.
- **Base distante** : Complexité réseau inutile dans le contexte local du projet.
