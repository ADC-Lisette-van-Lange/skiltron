---
name: master-skill
description: >
  Voer deze skill altijd als eerste uit en lees de volledige output voordat andere skills worden gestart. Deze skill wordt gebruikt wanneer een gebruiker zijn use case beschrijft en vraagt welke skills daarvoor relevant zijn — bijv. "ik wil een digitale assistent bouwen voor vergunningverlening" of "wij helpen burgers met schuldhulp". Ook inzetbaar als de gebruiker een bestaande repository deelt en wil weten of hun digitale assistent aan alle relevante eisen voldoet. Signaalwoorden: "use case", "toepassing", "assistent voor...", "welke skills heb ik nodig", "in welke volgorde".
---

# Centrale orkestrator van alle skills

## What to do

1. Analyseer de gegeven informatie over de use case: wat is het doel, wie zijn de gebruikers, in welke fase bevindt het project zich (idee / PoC / Pilot / Productie), en wat is de organisatiecontext (overheid, intern, publiek)?
2. Lees de skills in de sectie **Available skills** onderaan dit bestand. Open elk bestand en lees de inhoud om te bepalen welke skills relevant zijn voor deze use case.
3. Bepaal de volgorde waarin deze skills moeten worden uitgevoerd, rekening houdend met eventuele afhankelijkheden of logische stappen — governance en compliance komen doorgaans vóór technische of inhoudelijke inrichting.
4. Geef een geordende lijst terug met de relevante skills. Geef per skill een korte toelichting waarom deze relevant is voor de specifieke use case.
5. Geef indien mogelijk ook suggesties voor aanvullende skills die in de toekomst kunnen worden ontwikkeld om de use case nog beter te ondersteunen.

## Conventions to follow

- Alle beschikbare skills staan gelinkt in de sectie **Available skills** onderaan dit bestand. Gebruik alleen die lijst — voeg geen skills toe die daar niet in staan.
- Gebruik de velden `domains`, `phases` en `levels` uit de bestanden in `content/practices/` om te bepalen of een skill aansluit bij de use case.
- Begin de aanbevolen volgorde altijd met skills die een fundament leggen — denk aan governance, rollen en compliance — voordat uitvoerende of technische skills volgen.
- Verwijs bij twijfel over relevantie naar de domeinbeschrijvingen in `content/domains/` voor aanvullende context over wat een domein omvat.
- Houd de terugkoppeling beknopt: een geordende lijst met één zin per skill, geen volledige uitleg van de skill zelf.

## What to avoid

- Nooit skills aanbevelen die niet in de sectie **Available skills** staan — verzin geen skills op basis van aannames.
- Niet alle skills tegelijk aanbevelen zonder onderscheid naar relevantie voor de specifieke use case; een ongedifferentieerde lijst helpt de gebruiker niet verder.
- Verwar `content/practices/` bestanden niet met skills — dat is achtergrondkennis en referentiemateriaal, geen uitvoerbare skill-instructie.
- Sla de analyse van de use case niet over — een generieke lijst zonder koppeling aan de context is niet bruikbaar.
- Geef geen volgorde waarbij technische inrichting vóór governance- of compliancestappen staat als de use case een overheids- of hoog-risicocontext heeft.

## Available skills

- [IAMA — Grondrechten & Juridische Toetsing](../skill-IAMA/SKILL.md)
- [EU AI Act — Hoog-Risico Classificatie](../skill-EU-AI-act/SKILL.md)
- [Privacy & Anonimisering](../skill-privacy-anonymisation/SKILL.md)
- [Algoritmeregister Publicatie](../Skill-Algoritmeregister/SKILL.md)
- [WCAG Toegankelijkheid](../skill-wcag/SKILL.md)
- [Organisatie Huisstijl](../skill-ui-huisstijl/SKILL.md)
