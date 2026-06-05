from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import asyncio
import data
import llm

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.on_event("startup")
def startup():
    data.load()

CATEGORIEEN = [
    "Geluid", "Slaapverstoring", "Geur / luchtkwaliteit",
    "Meetwaarde / piekgeluid", "Baangebruik",
    "Structurele hinder", "Service / luchthavenervaring",
]

# --- Pagina 1: Intake ---

@app.get("/", response_class=HTMLResponse)
def intake_get(request: Request):
    return templates.TemplateResponse(
        request=request, name="intake.html",
        context={"categorieen": CATEGORIEEN, "success": False},
    )

@app.post("/", response_class=HTMLResponse)
def intake_post(
    request: Request,
    melder_naam: str = Form(""),
    email: str = Form(""),
    telefoon: str = Form(""),
    woonplaats: str = Form(""),
    postcodegebied: str = Form(""),
    klachtcategorie: str = Form(""),
    omschrijving: str = Form(""),
):
    melding_id = data.add_melding({
        "melder_naam": melder_naam,
        "email": email,
        "telefoon": telefoon,
        "woonplaats": woonplaats,
        "postcodegebied": postcodegebied,
        "klachtcategorie": klachtcategorie,
        "omschrijving": omschrijving,
        "datum_melding": "2026-06-04",
        "kanaal": "Webformulier",
    })
    return templates.TemplateResponse(
        request=request, name="intake.html",
        context={"categorieen": CATEGORIEEN, "success": True, "melding_id": melding_id},
    )

# --- Pagina 2: Meldingen ---

@app.get("/meldingen", response_class=HTMLResponse)
def meldingen(request: Request):
    return templates.TemplateResponse(
        request=request, name="meldingen.html",
        context={"meldingen": data.all_meldingen()},
    )

@app.get("/melding/{melding_id}", response_class=JSONResponse)
def melding_detail(melding_id: str):
    row = data.get_melding(melding_id)
    if not row:
        return JSONResponse({"error": "niet gevonden"}, status_code=404)
    row["conceptantwoord"] = data.get_conceptantwoord(row)
    row["routing"] = data.get_routing(row.get("klachtcategorie", ""))
    return JSONResponse(row)

# --- Chatbot ---

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    stats = data.dashboard_stats()
    dates = data.date_stats()
    context = (
        f"Totaal meldingen: {stats['totaal']}\n"
        f"Open: {stats['open']}, Gesloten: {stats['gesloten']}, Beantwoord: {stats['beantwoord']}\n"
        f"Per categorie: {stats['per_categorie']}\n"
        f"Per woonplaats (top 10): {stats['per_woonplaats']}\n"
        f"Datumrange: {dates['vroegste']} t/m {dates['laatste']}\n"
        f"Meldingen per maand: {dates['per_maand']}"
    )
    try:
        reply = await asyncio.to_thread(llm.chatbot, req.message, context)
    except Exception as e:
        return JSONResponse({"reply": f"Fout bij LLM: {e}"}, status_code=500)
    return JSONResponse({"reply": reply})


# --- Pagina 3: Data-assistent ---

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse(
        request=request, name="dashboard.html",
        context={},
    )
