---
id: iama-wettelijke-toetsing
title: Toets je IAMA aan de wettelijke verplichtingen uit de AI-verordening, AVG en Awb
summary: >
  Een goed uitgevoerd IAMA is noodzakelijk maar niet voldoende. Controleer of de
  uitkomsten van het IAMA aansluiten op de concrete wettelijke verplichtingen uit
  de EU AI-verordening, de AVG en de Algemene wet bestuursrecht — en leg de
  verbinding vast in een toetsingsdossier.
domains: [compliance, ethiek-mensenrechten, governance]
phases: [Pilot, Productie]
levels: [Compliance officer, Projectmanager]
sources:
  - iama
  - iama-toelichting
  - eu-ai-act
  - dpia-ap
  - algoritmekader-iama
---

## Waarom een aparte wettelijke toetsing naast het IAMA?

Het IAMA is een gespreksinstrument gericht op grondrechtelijke en ethische impact. Het dwingt niet automatisch af dat alle wettelijke verplichtingen worden gedekt. De AI-verordening, de AVG en de Awb stellen aanvullende, concrete eisen aan systemen die besluiten raken of persoonsgegevens verwerken. Zonder expliciete koppeling loopt je organisatie het risico dat het IAMA-traject wél is afgerond, maar wettelijke verplichtingen alsnog worden gemist.

---

## Stap 1 — Classificeer het systeem onder de AI-verordening

Bepaal de risicocategorie van de assistent vóór de IAMA-uitvoering:

- **Onaanvaardbaar risico** (verboden): realtime biometrische identificatie in openbare ruimten, sociale scoresystemen, manipulatieve technieken gericht op kwetsbare groepen.
- **Hoog risico** (bijlage III AI-verordening): systemen die besluiten ondersteunen over uitkeringen, vergunningen, schuldhulp, toelating tot voorzieningen of strafrechtelijke context. Bij hoog risico gelden verplichte conformiteitsbeoordeling, menselijk toezicht, logregistratie en registratie in de EU-database.
- **Beperkt risico**: chatbots en generatieve AI met transparantieplicht — gebruikers moeten weten dat zij met een AI-systeem communiceren.
- **Minimaal risico**: geen specifieke verplichtingen, maar documentatie blijft aanbevolen.

Leg de classificatie vast met motivering; bij twijfel tussen categorieën geldt de hogere categorie.

---

## Stap 2 — Koppel IAMA-uitkomsten aan specifieke wetsartikelen

Gebruik onderstaande kruistabel als checklist. Markeer per rij of het punt in het IAMA is besproken en of de wettelijke verplichting daadwerkelijk is geborgd.

| IAMA-thema | Relevante wetgeving | Concrete verplichting |
|---|---|---|
| Doelbinding en noodzakelijkheid | AVG art. 5 lid 1 sub b en c | Verwerkingsdoel omschreven, geen verdere verwerking buiten doel |
| Grondslag voor verwerking persoonsgegevens | AVG art. 6 / art. 9 (bijzondere cat.) | Geldige grondslag per gegevenstype vastgesteld |
| Geautomatiseerde besluitvorming | AVG art. 22 | Menselijke tussenkomst geregeld of uitzondering gemotiveerd |
| Transparantie naar burger | AI-verordening art. 50 / AVG art. 13-14 | Gebruikersinformatie over AI-gebruik aanwezig |
| Menselijk toezicht | AI-verordening art. 14 (hoog risico) | Toezichtmechanisme beschreven en belegd |
| Logging en auditbaarheid | AI-verordening art. 12 (hoog risico) | Loggen van relevante besluiten ingericht |
| Non-discriminatie | Awb art. 2:4 / EVRM art. 14 | Biascheck uitgevoerd, uitkomsten gedocumenteerd |
| Betrokkenenrechten | AVG art. 15-22 | Procedure voor inzage, correctie en bezwaar beschikbaar |
| Verantwoordingsplicht | AVG art. 5 lid 2 | Verwerkingsregister bijgewerkt |
| Rechtsmiddelenclausule | Awb afd. 3.7 / art. 3:46-3:50 | Besluiten voldoende gemotiveerd, bezwaar mogelijk |

---

## Stap 3 — Stel het toetsingsdossier samen

Het toetsingsdossier bewijst bij een audit of handhavingsonderzoek dat de wettelijke analyse is uitgevoerd. Neem hierin op:

1. **Classificatiebesluit** — AI-risicocategorie met motivering.
2. **Kruistabelresultaat** — welke verplichtingen zijn gedekt, welke open staan met actiehouder en deadline.
3. **DPIA-uitkomst** (indien van toepassing) — samenvatting en resterende risico's.
4. **IAMA-verslag** — kernbevindingen en afspraken.
5. **Menselijk toezichtplan** — wie keurt welke output goed, bij welke drempelwaarden.
6. **Registratiebewijs** — uittreksel uit het verwerkingsregister en eventueel de EU-AI-database.

Bewaar het dossier minimaal zolang het systeem in gebruik is plus vijf jaar; bij hoog-risicosystemen tien jaar (AI-verordening art. 18).

---

## Stap 4 — Herhaal bij elke materiële wijziging

Wettelijke toetsing is geen eenmalige activiteit. Heropen het dossier en herhaal stap 1 t/m 3 bij:

- Een nieuw gebruik van de assistent buiten het oorspronkelijke doel.
- Koppeling met nieuwe databronnen of systemen.
- Uitbreiding van de doelgroep (intern → extern, of nieuw type burger).
- Een gewijzigd model of nieuwe modelversie met andere outputs.
- Signalen uit monitoring over bias, fouten of klachten van burgers.

Leg de herbeoordeling met datum en uitkomst vast in het dossier.

---

## Valkuilen

- **IAMA afvinken zonder wetscheck**: het IAMA-gesprek is waardevol, maar dekt niet automatisch art. 22 AVG of de hoog-risico-eisen uit de AI-verordening. Combineer altijd beide.
- **Classificatie te laag inschatten**: twijfel over risicocategorie is een signaal voor de hogere categorie, niet de lagere — de bewijslast voor een lagere classificatie ligt bij de organisatie.
- **Toetsingsdossier niet actueel houden**: een oud dossier is erger dan geen dossier; het wekt de schijn van compliance terwijl de werkelijkheid is veranderd.
- **Menselijk toezicht op papier**: een toezichtprocedure die in de praktijk niet wordt gevolgd, telt juridisch niet mee als borgingsmaatregel.
