# Analyse des besoins – Système de caisse 2-tiers (POS)

## 1. Présentation du système

Le système à développer est une application de caisse (Point Of Sale) pour un petit magasin de quartier. Il doit permettre aux employés d’effectuer les opérations de vente, de gérer les stocks, et d’assurer le bon déroulement des transactions via une application console connectée directement à une base de données locale.

---

## 2. Besoins fonctionnels

Le système doit permettre :

1. **Rechercher un produit**
   - Par identifiant (ID unique)
   - Par nom de produit
   - Par catégorie

2. **Enregistrer une vente**
   - Sélection de produits et quantités
   - Calcul automatique du total (montant)
   - Décrémentation du stock pour chaque produit vendu
   - Enregistrement de la transaction (date, produits, quantités, montant, caisse utilisée)

3. **Gérer les retours/annuler une vente**
   - Identifier une vente à annuler (ID de vente)
   - Rétablir le stock correspondant
   - Archiver la vente annulée pour historique

4. **Consulter l’état du stock**
   - Afficher le stock actuel de tous les produits
   - Rechercher le stock d’un produit précis

5. **Gestion multi-caisses**
   - Support de plusieurs caisses en simultané (au moins 3)
   - Transactions atomiques : éviter les conflits et garantir la cohérence du stock

---

## 3. Besoins non-fonctionnels

- **Simplicité d’utilisation**
  - Interface console claire, instructions explicites pour l’utilisateur

- **Robustesse et fiabilité**
  - Gestion des erreurs utilisateur (saisie invalide, stock insuffisant…)
  - Transactions sûres : toute opération critique doit être atomique

- **Persistance fiable**
  - Utilisation d’un ORM pour simplifier la gestion des données
  - Stockage local (SQLite ou autre SGBD simple)

- **Portabilité**
  - Exécution facile sur tout environnement (Windows, Mac, Linux)
  - Utilisation de Docker pour faciliter le déploiement

- **Sécurité basique**
  - Protection contre les accès concurrents et les incohérences de stock

- **Extensibilité**
  - Base de code conçue pour être évolutive (ex : ajout futur de fonctionnalités, gestion multi-magasins, passage à une interface graphique, etc.)

---

## 4. Contraintes

- Le système doit être livré sous forme de code source, accompagné de sa documentation (README, ADRs, diagrammes UML)
- L’application doit être conteneurisée avec Docker, et orchestrée avec docker-compose (BDD + app)
- Les pratiques de CI/CD (tests, build, lint) doivent être respectées comme dans le laboratoire précédent

---

## 5. Résumé des cas d’utilisation principaux

- Rechercher produit
- Enregistrer une vente
- Annuler/retourner une vente
- Consulter l’état du stock

