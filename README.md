# Building Skills – Digitale Assistent

---

## Inhoudsopgave

1. [Over dit project](#over-dit-project)
2. [Projectstructuur](#projectstructuur)
3. [Use case](#use-case)
4. [Skills](#skills)
5. [Installatie](#installatie)

---

## Over dit project

Dit project ondersteunt overheidsteams bij het verantwoord ontwikkelen van digitale assistenten. Het bevat:

- **Claude Code skills** voor gestructureerde begeleiding tijdens ontwikkeling
- Een **use case** als initeel voorbeeld, zonder Claude code skills
- Een **adjusted use case ** als voorbeeld waarin de wijzigingen met Claude Code-skills zijn verwerkt

---

## Projectstructuur

```
├── claude/skills/     # Claude Code skills
├── use-case/           # Demo-applicatie (klachtenmeldingen luchthaven)
└── use-case-adjusted/  # Aangepaste versie van de demo
```

---

## Use case

De use case is een **FastAPI-webapplicatie** voor het afhandelen van klachtenmeldingen rondom een luchthaven. Ze bevat drie onderdelen:

| Pagina | Route | Omschrijving |
|---|---|---|
| Intake | `/` | Burger dient een melding in |
| Meldingen | `/meldingen` | Overzicht van alle meldingen |
| Dashboard | `/dashboard` | Statistieken en AI-chatbot |

De chatbot gebruikt de OpenAI API (via GreenPT) en krijgt dashboarddata als context mee.

---

## Skills

De skills in `.claude/skills/` begeleiden ontwikkelaars stap voor stap langs relevante eisen en aandachtspunten:

| Skill | Omschrijving |
|---|---|
| `master-skill` | Startpunt – bepaalt welke skills relevant zijn |
| `skill-EU-AI-act` | Classificatie en verplichtingen onder de EU AI Act |
| `skill-Algoritmeregister` | Publicatie in het Nederlandse Algoritmeregister |
| `skill-privacy-anonymisation` | AVG-conforme verwerking van persoonsgegevens |
| `skill-human-in-the-loop` | Menselijk toezicht inrichten |
| `skill-IAMA` | Impact Assessment Mensenrechten en Algoritmen |
| `skill-rag-pijplijn` | RAG-architectuur opzetten |
| `skill-rag-evaluatie` | Kwaliteitsbeoordeling van RAG-systemen |
| `skill-kleinste-model` | Modelkeuze optimaliseren |
| `skill-ui-huisstijl` | Rijkshuisstijl toepassen |
| `skill-wcag` | Toegankelijkheid (WCAG) |

---

## Installatie

1. **Kloon de repository en maak een virtual environment aan**

```bash
git clone <repo-url>
cd building-skills-digital-assistant
python -m venv venv
source venv/bin/activate
```

2. **Installeer de dependencies**

```bash
pip install -r use-case/requirements.txt
```

3. **Stel de omgevingsvariabelen in**

Kopieer `.env_example` naar `.env` en vul je API-sleutel in:

```bash
cp .env_example .env
```

4. **Start de applicatie**

Use case (poort 8000):
```bash
cd use-case
uvicorn main:app --reload
```

Use case adjusted (poort 8001):
```bash
cd use-case-adjusted
uvicorn main:app --reload --port 8001
```

De use-case is beschikbaar op `http://localhost:8000`.
De use-case-adjusted is beschikbaar op `http://localhost:8001`.
