from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from magasin.services import (
    consulter_stock_magasin, performances_magasin, generer_performances_magasin
)
from logistique.services import (
    consulter_stock_logistique, verifier_et_reapprovisionner, approvisionner_magasin
)
from maison_mere.services import generer_rapport_ventes
from magasin.models import Produit
from common.database import SessionLocal

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    stock = consulter_stock_logistique()
    return templates.TemplateResponse("index.html", {"request": request, "stock": stock})


@app.get("/rapport", response_class=HTMLResponse)
def afficher_rapport(request: Request):
    data = generer_rapport_ventes()
    return templates.TemplateResponse("rapport.html", {"request": request, "data": data})


@app.get("/performances", response_class=HTMLResponse)
def afficher_performances(request: Request):
    data = generer_performances_magasin()
    return templates.TemplateResponse("performances.html", {"request": request, "result": data})


@app.get("/maj_produit", response_class=HTMLResponse)
def afficher_formulaire_maj(request: Request):
    db = SessionLocal()
    produits = db.query(Produit).all()
    db.close()
    return templates.TemplateResponse("maj_produit.html", {"request": request, "produits": produits})




@app.post("/maj_produit", response_class=HTMLResponse)
def mettre_a_jour_produit(request: Request, produit_id: int = Form(...), nom: str = Form(...), prix: float = Form(...), description: str = Form(...)):
    db = SessionLocal()
    produit = db.query(Produit).filter_by(id=produit_id).first()
    if produit:
        produit.nom = nom
        produit.prix = prix
        produit.description = description
        db.commit()

    produits = db.query(Produit).all()
    db.close()
    return templates.TemplateResponse("maj_produit.html", {
        "request": request,
        "message": "Produit mis à jour avec succès.",
        "produits": produits
    })




@app.post("/execute", response_class=HTMLResponse)
async def execute_action(request: Request):
    form_data = await request.form()
    action = form_data.get("action")
    section = form_data.get("section", None)

    result = None
    stock_magasin = None

    try:
        if action == "rapport":
            return RedirectResponse(url="/rapport", status_code=303)

        elif action == "performances":
            result = performances_magasin()

        elif action == "reapprovisionnement":
            produit_id = int(form_data.get("produit_id"))
            quantite = int(form_data.get("quantite"))
            magasin_id = int(form_data.get("magasin_id"))
            result = verifier_et_reapprovisionner(magasin_id, produit_id, quantite)

        elif action == "approvisionner":
            produit_id = int(form_data.get("produit_id"))
            quantite = int(form_data.get("quantite"))
            result = approvisionner_magasin(produit_id, quantite)

        elif action == "consulter_stock_magasin":
            magasin_id = int(form_data.get("magasin_id"))
            stock_magasin = consulter_stock_magasin(magasin_id)

        else:
            result = "Action non reconnue."

    except Exception as e:
        result = f"Erreur : {str(e)}"

    stock = consulter_stock_logistique()
    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": result,
        "stock": stock,
        "stock_magasin": stock_magasin,
        "active_section": section
    })
