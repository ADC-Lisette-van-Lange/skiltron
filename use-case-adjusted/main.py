from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List
from pathlib import Path
from datetime import date
import asyncio, io, re
import data
import llm
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, HRFlowable, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader

BRAND       = HexColor('#a3195b')
BRAND_LIGHT = HexColor('#ecdfe6')
MUTED       = HexColor('#7a6a73')
INK         = HexColor('#1a1119')
LOGO_PATH   = Path(__file__).parent / "static" / "logo-gemeente-aalsmeer.png"
DUTCH_MONTHS = ["januari","februari","maart","april","mei","juni",
                "juli","augustus","september","oktober","november","december"]

def _datum_nl(d: date) -> str:
    return f"{d.day} {DUTCH_MONTHS[d.month-1]} {d.year}"

def _logo_img():
    if not LOGO_PATH.exists():
        return None
    reader = ImageReader(str(LOGO_PATH))
    iw, ih = reader.getSize()
    w = 5 * cm
    h = w * ih / iw
    img = Image(str(LOGO_PATH), width=w, height=h)
    img.hAlign = 'LEFT'
    return img

def _make_style(ss, name, **kw):
    s = ParagraphStyle(name, parent=ss['Normal'])
    for k, v in kw.items():
        setattr(s, k, v)
    return s

def genereer_pdf(memo_tekst: str) -> bytes:
    buf = io.BytesIO()
    doc = SimpleDocTemplate(
        buf, pagesize=A4,
        rightMargin=2.5*cm, leftMargin=2.5*cm,
        topMargin=2*cm, bottomMargin=2*cm,
    )
    ss = getSampleStyleSheet()
    title_s  = _make_style(ss, 'mtitle',  fontSize=20, textColor=BRAND, fontName='Helvetica-Bold', leading=26, spaceAfter=10)
    meta_s   = _make_style(ss, 'mmeta',   fontSize=9,  textColor=MUTED, spaceAfter=2)
    h2_s     = _make_style(ss, 'mh2',     fontSize=11, textColor=BRAND, fontName='Helvetica-Bold', spaceBefore=14, spaceAfter=4)
    body_s   = _make_style(ss, 'mbody',   fontSize=10, leading=15, spaceAfter=6, textColor=INK)
    bullet_s = _make_style(ss, 'mbullet', fontSize=10, leading=15, spaceAfter=4, textColor=INK, leftIndent=12)
    footer_s = _make_style(ss, 'mfooter', fontSize=8,  textColor=MUTED)
    date_s   = _make_style(ss, 'mdate',   fontSize=9,  textColor=MUTED, alignment=2)

    story = []

    # Header row: logo left, date right
    datum_str = _datum_nl(date.today())
    logo = _logo_img()
    if logo:
        tbl = Table([[logo, Paragraph(datum_str, date_s)]], colWidths=[11*cm, 4.5*cm])
        tbl.setStyle(TableStyle([
            ('VALIGN',  (0,0), (-1,-1), 'MIDDLE'),
            ('ALIGN',   (1,0), (1,0),   'RIGHT'),
            ('LEFTPADDING',  (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ]))
        story.append(tbl)
    else:
        story.append(Paragraph(datum_str, date_s))

    story.append(Spacer(1, 0.4*cm))
    story.append(HRFlowable(width="100%", thickness=2, color=BRAND, spaceAfter=8))
    story.append(Paragraph("MEMO", title_s))
    story.append(Paragraph("Gemeente Aalsmeer · Afdeling Beleid &amp; Ruimte", meta_s))
    story.append(Paragraph(f"Datum: {datum_str}", meta_s))
    story.append(HRFlowable(width="100%", thickness=0.5, color=BRAND_LIGHT, spaceBefore=6, spaceAfter=10))

    # Strip leading MEMO heading if LLM included it anyway
    lines_raw = memo_tekst.split('\n')
    while lines_raw and lines_raw[0].strip().upper().lstrip('#').strip() == 'MEMO':
        lines_raw.pop(0)
    memo_tekst = '\n'.join(lines_raw)

    # Parse LLM output line by line
    for line in memo_tekst.split('\n'):
        s = line.strip()
        if not s:
            story.append(Spacer(1, 0.15*cm))
            continue
        if s.startswith('## '):
            story.append(Paragraph(s[3:], h2_s))
        elif s.startswith('# '):
            story.append(Paragraph(s[2:], h2_s))
        elif s.startswith('**') and s.endswith('**') and len(s) > 4:
            story.append(Paragraph(f'<b>{s[2:-2]}</b>', h2_s))
        elif s.startswith('- ') or s.startswith('* '):
            content = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', s[2:])
            story.append(Paragraph(f'• {content}', bullet_s))
        else:
            content = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', s)
            story.append(Paragraph(content, body_s))

    story.append(Spacer(1, 1*cm))
    story.append(HRFlowable(width="100%", thickness=0.5, color=BRAND_LIGHT))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph("Gemeente Aalsmeer · Schiphol Signalen · Vertrouwelijk intern document", footer_s))

    doc.build(story)
    return buf.getvalue()

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
def index(request: Request):
    return templates.TemplateResponse(
        request=request, name="meldingen.html",
        context={"meldingen": data.all_meldingen()},
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


# --- Pagina 4: Memo generator ---

@app.get("/memo", response_class=HTMLResponse)
def memo_get(request: Request):
    return templates.TemplateResponse(request=request, name="memo.html", context={})

@app.post("/memo/genereer")
async def memo_genereer(
    doelgroep: str = Form(""),
    vraagstuk: str = Form(""),
    scope: str = Form(""),
    doel_richting: str = Form(""),
):
    if not any([doelgroep.strip(), vraagstuk.strip(), scope.strip(), doel_richting.strip()]):
        return JSONResponse({"error": "Vul minimaal één veld in."}, status_code=400)

    stats = data.dashboard_stats()
    dates = data.date_stats()

    cat_lines  = "\n".join(f"- {c['klachtcategorie']}: {c['aantal']}" for c in stats['per_categorie'])
    wp_lines   = "\n".join(f"- {w['woonplaats']}: {w['aantal']}" for w in stats['per_woonplaats'])
    trend_lines= "\n".join(f"- {k}: {v}" for k, v in dates['per_maand'].items())
    rec_lines  = "\n".join(
        f"- {r['datum_melding']} | {r['klachtcategorie']} | {r['woonplaats']} | {r['status']}"
        for r in stats['recente']
    )

    data_context = (
        f"Totaal meldingen: {stats['totaal']}\n"
        f"Open: {stats['open']}, Gesloten: {stats['gesloten']}, Beantwoord: {stats['beantwoord']}\n\n"
        f"Meldingen per categorie:\n{cat_lines}\n\n"
        f"Meldingen per woonplaats (top 10):\n{wp_lines}\n\n"
        f"Tijdtrend per maand (periode {dates['vroegste']} t/m {dates['laatste']}):\n{trend_lines}\n\n"
        f"Recente meldingen:\n{rec_lines}"
    )

    instructies = (
        f"Doelgroep: {doelgroep}\n"
        f"Vraagstuk: {vraagstuk}\n"
        f"Scope: {scope}\n"
        f"Doel & richting: {doel_richting}"
    )

    try:
        memo_tekst = await asyncio.to_thread(llm.genereer_memo, instructies, data_context)
    except Exception as e:
        return JSONResponse({"error": f"LLM fout: {e}"}, status_code=500)

    try:
        pdf_bytes = genereer_pdf(memo_tekst)
    except Exception as e:
        return JSONResponse({"error": f"PDF fout: {e}"}, status_code=500)

    return StreamingResponse(
        io.BytesIO(pdf_bytes),
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=memo-gemeente-aalsmeer.pdf"},
    )


# --- Pagina 3: Dashboard ---

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse(
        request=request, name="dashboard.html",
        context={},
    )
