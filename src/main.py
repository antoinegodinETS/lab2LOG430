from db import init_db
from repository import ajouter_produit, lister_produits, annuler_vente, enregistrer_vente, lister_ventes
from tabulate import tabulate


def menu():
    while True:
        print("\n=== Système de caisse POS ===")
        print("1. Ajouter un produit")
        print("2. Lister les produits")
        print("3. Enregistrer une vente")
        print("4. Lister les ventes")
        print("5. Annuler une vente")
        print("6. Quitter")
        choix = input("Votre choix : ")

        if choix == "1":
            nom = input("Nom du produit : ")
            categorie = input("Catégorie : ")
            prix = float(input("Prix : "))
            stock = int(input("Stock : "))
            ajouter_produit(nom, categorie, prix, stock)
            print("Produit ajouté.")
            pass
        elif choix == "2":
            produits = lister_produits()
            table = [[p.id, p.nom, p.categorie, p.prix, p.stock]
                     for p in produits]
            print(
                tabulate(
                    table,
                    headers=[
                        "ID",
                        "Nom",
                        "Catégorie",
                        "Prix",
                        "Stock"]))
            pass
        elif choix == "3":
            produits = lister_produits()
            table = [[p.id, p.nom, p.categorie, p.prix, p.stock]
                     for p in produits]
            print(
                tabulate(
                    table,
                    headers=[
                        "ID",
                        "Nom",
                        "Catégorie",
                        "Prix",
                        "Stock"]))
            print("Entrer les articles (ID et quantité), vide pour terminer.")
            articles = []
            while True:
                pid = input("ID produit (vide pour finir) : ")
                if not pid:
                    break
                qte = input("Quantité : ")
                try:
                    pid = int(pid)
                    qte = int(qte)
                except ValueError:
                    print("Entrée invalide.")
                    continue
                articles.append((pid, qte))
            caisse_num = int(input("Numéro de caisse (1-3) : "))
            ok, msg = enregistrer_vente(articles, caisse_num)
            print(msg)
        elif choix == "4":
            ventes = lister_ventes()
            table = [[v.id,
                      v.date.strftime('%Y-%m-%d %H:%M:%S'),
                      v.total,
                      v.caisse,
                      "Oui" if v.annulee else "Non"] for v in ventes]
            print(
                tabulate(
                    table,
                    headers=[
                        "ID",
                        "Date",
                        "Total",
                        "Caisse",
                        "Annulée"]))
        elif choix == "5":
            vente_id = input("ID de la vente à annuler : ")
            try:
                vente_id = int(vente_id)
            except ValueError:
                print("ID invalide.")
                continue
            ok, msg = annuler_vente(vente_id)
            print(msg)
        elif choix == "6":
            break
        else:
            print("Choix invalide.")


if __name__ == "__main__":
    init_db()
    menu()
