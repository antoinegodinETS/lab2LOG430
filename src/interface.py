from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from magasin.services import consulter_stock_magasin, performances_magasin, generer_rapport_ventes
from logistique.services import consulter_stock_logistique, verifier_et_reapprovisionner, approvisionner_magasin
from maison_mere.services import mettre_a_jour_produit

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/rapport", response_class=HTMLResponse)
def afficher_rapport(request: Request):
    data = generer_rapport_ventes()
    return templates.TemplateResponse("rapport.html", {"request": request, "data": data})


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    stock = consulter_stock_logistique()  # Charger le stock logistique au départ
    return templates.TemplateResponse("index.html", {"request": request, "stock": stock})

@app.post("/execute", response_class=HTMLResponse)
async def execute_action(request: Request):
    form_data = await request.form()
    action = form_data.get("action")
    section = form_data.get("section", None)

    result = None
    stock_magasin = None  # Initialisation pour éviter les conflits

    try:
        if action == "rapport":
            return RedirectResponse(url="/rapport", status_code=303)

        elif action == "performances":
            result = performances_magasin()

        elif action == "maj_produit":
            produit_id = int(form_data.get("produit_id"))
            nouvelles_infos = form_data.get("nouvelles_infos")
            result = mettre_a_jour_produit(produit_id, nouvelles_infos)

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

    stock = consulter_stock_logistique()  # Toujours afficher le stock logistique

    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": result,
        "stock": stock,
        "stock_magasin": stock_magasin,
        "active_section": section
    })
