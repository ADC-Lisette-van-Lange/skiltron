/master-skill look at the use case and check if there are any skills i can use to make the digital assistant better                                                                                                                                                                                                                                                                                                                                                      

⏺ I'll read the use case files to understand what the digital assistant does before analyzing which skills apply.
                                
  Read 4 files (ctrl+o to expand)

⏺ Now I have a clear picture. Let me analyze which skills apply.

  ---
  Analyse: Schiphol Signalen — Gemeente Aalsmeer
  
  De use case is een gemeentelijk meldingssysteem voor Schiphol-overlast met drie onderdelen:
  - Publiek intakeformulier (burgers dienen meldingen in)
  - Intern dashboard + meldingenoverzicht (gemeente-medewerkers)
  - AI-chatbot (data-assistent op het dashboard)
  
  De code bevat al twee expliciete commentaren # foute versie die privacy-issues markeren. Dit beïnvloedt de prioritering.

  ---
  Aanbevolen skills — in volgorde
  
  1. Privacy & Anonimisering — direct uitvoeren

  Waarom relevant: De code bevat twee aangemerkte privacy-fouten:
  - data.py:89 — recente records op het dashboard bevatten melder_naam, email en omschrijving (directe persoonsgegevens)
  - data.py:68 — per_woonplaats toont aantallen ook onder de 5, wat herleidbaar kan zijn naar individuen
  - De chatbot-context (main.py:87-94) stuurt per_woonplaats (top 10) door naar het LLM

  Waarmee het helpt: Dwingt een harde scheiding af tussen de pseudonieme verwerkingslaag (individuele meldingsafhandeling) en een volledig anonieme inzichtenlaag (dashboard/chatbot). Je krijgt concrete regels voor k-anonimiteit (minimumdrempel per groep) en AVG-grondslag voor de verwerking van naam, e-mail en telefoon.

  Wanneer: Nu — vóór verdere uitbreiding van het dashboard of de chatbot.

  ---
  2. EU AI Act — Risicoklassificatie

  Waarom relevant: Het systeem bevat twee AI-componenten: een LLM-chatbot (llm.py) voor intern gebruik, en een automatische routering + concept-antwoordgeneratie (data.py:13-36). Als de concept-antwoorden of routing invloed hebben op hoe burgermeldingen worden behandeld, raakt dit potentieel aan "toegang tot publieke dienstverlening" (Annex III).

  Waarmee het helpt: Een onderbouwd oordeel of het systeem minimaal-risico of beperkt-risico is (met transparantieverplichtingen voor de chatbot), en of de routing als impactvol algoritme geldt. Voorkomt dat je later onverwacht verplichtingen mist richting productie.

  Wanneer: Vóór de IAMA en vóór livegang.

  ---
  3. IAMA — Grondrechten & Juridische Toetsing
  
  Waarom relevant: Gemeente Aalsmeer is een overheidsorgaan dat persoonsgegevens van burgers verwerkt in een klachtenproces dat doorwerkt in bestuurlijke rapportages richting het Rijk (data.py:30). De automatische routing bepaalt welke afdeling een melding behandelt — dit beïnvloedt de afhandeling van burgersignalen.

  Waarmee het helpt: Screeningsvragen voor grondrechtelijke impact (privacy, non-discriminatie bij routing), een dossieropzet en doorverwijzing naar FG en juridisch adviseur van de gemeente.

  Wanneer: Na de EU AI Act-classificatie, vóór pilotfase.

  ---
  4. Menselijke Controle

  Waarom relevant: De concept-antwoorden worden volledig automatisch gegenereerd op basis van categorie (data.py:25-36) en direct zichtbaar gemaakt aan medewerkers via melding_detail (main.py:74). Er is geen expliciete goedkeuringsstap of override-mechanisme ingebouwd voordat een antwoord verstuurd wordt.

  Waarmee het helpt: Een menselijk toezichtplan met escalatiepad, een override-bediening in de UI, logboek van menselijke beslissingen, en een RACI-matrix. Concreet: wie mag een concept-antwoord goedkeuren voordat het naar de burger gaat?

  Wanneer: Bij de bouw van de afhandelingsflow, vóór productie.

  ---
  5. WCAG Toegankelijkheid

  Wanneer: Vóór de IAMA en vóór livegang.

  ---
  3. IAMA — Grondrechten & Juridische Toetsing


  Waarom relevant: Gemeente Aalsmeer is een overheidsorgaan dat persoonsgegevens van burgers verwerkt in een klachtenproces dat doorwerkt in bestuurlijke rapportages richting het Rijk (data.py:30). De automatische routing bepaalt welke afdeling een melding behandelt — dit beïnvloedt de afhandeling van burgersignalen.

  Waarmee het helpt: Screeningsvragen voor grondrechtelijke impact (privacy, non-discriminatie bij routing), een dossieropzet en doorverwijzing naar FG en juridisch adviseur van de gemeente.

  Wanneer: Na de EU AI Act-classificatie, vóór pilotfase.


  Waarom relevant: De concept-antwoorden worden volledig automatisch gegenereerd op basis van categorie (data.py:25-36) en direct zichtbaar gemaakt aan medewerkers via melding_detail (main.py:74). Er is geen expliciete goedkeuringsstap of override-mechanisme ingebouwd voordat een antwoord verstuurd wordt.

  Waarmee het helpt: Een menselijk toezichtplan met escalatiepad, een override-bediening in de UI, logboek van menselijke beslissingen, en een RACI-matrix. Concreet: wie mag een concept-antwoord goedkeuren voordat het naar de burger gaat?


  Wanneer: Bij de bouw van de afhandelingsflow, vóór productie.
  ---
  5. WCAG Toegankelijkheid

  Waarmee het helpt: Testresultaten voor contrast, toetsenbordnavigatie en schermlezer op het intakeformulier, plus een plan voor de toegankelijkheidsverklaring.

  Wanneer: Bij afronden van de UI, vóór publieke livegang.

  ---

  ---
  Waarmee het helpt: Een ingevuld registratieformulier (tekst + JSON) klaar voor upload naar algoritmes.overheid.nl.

  Waarmee het helpt: Een ingevuld registratieformulier (tekst + JSON) klaar voor upload naar algoritmes.overheid.nl.

  Wanneer: Na afronding van EU AI Act-classificatie en IAMA, bij productiegang.

  ---
  7. Organisatie Huisstijl

  Waarom relevant: De UI gebruikt al --aalsmeer-blauw: #005b9e (base.html:10) maar heeft geen formeel tokenbestand. Als Gemeente Aalsmeer een officiële huisstijlgids heeft (logo, typografie, kleurenpalet), past de huidige implementatie die mogelijk niet volledig toe.

  Waarmee het helpt: Een tokenbestand met kleuren, lettertype en logo van de gemeente, gekoppeld aan de interface — zodat de huisstijl consistent en onderhoudbaar is.

  Wanneer: Bij verdere UI-ontwikkeling.

  ---
  8. Kleinste Model per Taak

  Waarom relevant: De chatbot gebruikt nu één model (gemma4 via GreenPT) voor alle vragen. Eenvoudige statistiekvragen ("hoeveel meldingen zijn er open?") vereisen minder capaciteit dan complexe analysesvragen. Een configuratie per taak bespaart kosten en latentie.

  Waarmee het helpt: Een configuratiebestand waarin per taaktype staat welk model je inzet.

  Wanneer: Na stabilisatie van de functionaliteit, bij optimalisatie richting productie.

  ---
  Suggestie voor toekomstige skill

  RAG-pijplijn evaluatie (skill-rag-evaluatie): als de chatbot in de toekomst niet alleen op aggregaatstatistieken maar ook op de volledige meldingsteksten gaat antwoorden, is een RAG-evaluatieskill relevant om de kwaliteit en hallucination-risico's te meten.