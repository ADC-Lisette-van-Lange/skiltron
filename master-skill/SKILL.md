---
id: master-skill
title: Centrale orkestrator van alle skills voor deze use case
summary: >
  Deze skill beheert en structureert alle relevante deel-skills die nodig zijn voor deze specifieke use case. Hij fungeert als centrale orkestrator: op basis van de gebruikersvraag bepaalt hij welke onderliggende skills worden aangesproken, in welke volgorde zij worden uitgevoerd en hoe hun resultaten worden gecombineerd tot één samenhangend antwoord. Hierdoor blijft de logica overzichtelijk, herbruikbaar en eenvoudig uit te breiden met nieuwe skills.
---

# Centrale orkestrator van alle skills

## When to use this Skill

Gebruik deze skill wanneer een gebruiker zijn use case beschrijft en vraagt welke skills daarvoor relevant zijn. Concrete signalen:

- De gebruiker beschrijft een situatie, probleem of doel — bijv. "ik wil een digitale assistent bouwen voor vergunningverlening" of "wij helpen burgers met schuldhulp".
- De gebruiker vraagt expliciet welke skills hij nodig heeft, of welke hij moet doorlopen.
- De gebruiker wil weten in welke volgorde hij de beschikbare skills moet inzetten.
- De gebruiker gebruikt woorden als "use case", "toepassing", "assistent voor...", "scenario", of "ik wil bereiken dat...".
- De gebruiker deelt een bestaande repository en wil weten of hun digitale assistent aan alle relevante eisen voldoet — gebruik dan deze skill om te bepalen welke skills als audit ingezet kunnen worden om dit te controleren.

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

- [IAMA Wettelijke Toetsing](../IAMA-skill/SKILL.md)
- [Privacy & Anonimisering](../privacy-anonymisation-skill/SKILL.md)
