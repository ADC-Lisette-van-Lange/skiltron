import os
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent / ".env")

client = OpenAI(
    api_key=os.environ["GREENPT_API_KEY"],
    base_url="https://api.greenpt.ai/v1",
    timeout=30.0,
)


def genereer_memo(instructies: str, data_context: str) -> str:
    response = client.chat.completions.create(
        model="gemma4",
        messages=[
            {
                "role": "system",
                "content": (
                    "Je bent een beleidsassistent voor Gemeente Aalsmeer. "
                    "Schrijf een professioneel ambtelijk memo op basis van de instructies en de meegeleverde data.\n\n"

                    "STRIKTE REGELS — deze gelden altijd en zonder uitzondering:\n"
                    "1. Gebruik UITSLUITEND cijfers, percentages en feiten die letterlijk in de meegeleverde data staan. "
                    "Verzin geen statistieken, aantallen, trends of conclusies die niet direct uit de data volgen.\n"
                    "2. Noem NOOIT namen van personen, e-mailadressen, telefoonnummers of andere gegevens "
                    "waarmee een individu te identificeren is — ook niet als voorbeeld of fictief geval.\n"
                    "3. Gebruik geen informatie uit je trainingsdata over Schiphol, geluidsnormen of beleid "
                    "tenzij die expliciet in de meegeleverde data staat.\n"
                    "4. Als de data onvoldoende is om een bewering te onderbouwen, schrijf dat dan expliciet "
                    "(bijv. 'Op basis van de beschikbare data kan hierover geen uitspraak worden gedaan.').\n\n"

                    "OPMAAKREGELS:\n"
                    "- Gebruik duidelijke koppen (beginnen met ##), alinea's en een heldere structuur.\n"
                    "- Schrijf in het Nederlands in een formele ambtelijke stijl.\n"
                    "- Begin met een korte inleiding, verwerk de data in de tekst en sluit af met een conclusie of aanbeveling.\n"
                    "- Gebruik **vetgedrukte tekst** voor belangrijke begrippen.\n"
                    "- Gebruik geen markdown-tabel — gebruik gewone tekst of opsommingen.\n"
                    "- Begin NIET met 'MEMO' als eerste regel — dat wordt automatisch toegevoegd."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Instructies voor het memo:\n{instructies}\n\n"
                    f"Beschikbare data:\n{data_context}"
                ),
            },
        ],
        stream=False,
    )
    return response.choices[0].message.content


def chatbot(message: str, context: str) -> str:
    response = client.chat.completions.create(
        model="gemma4",
        messages=[
            {
                "role": "system",
                "content": (
                    "Je bent een data-assistent voor Gemeente Aalsmeer. "
                    f"Je hebt toegang tot de volgende meldingsdata:\n{context}\n"
                    "Beantwoord vragen over de data beknopt en in het Nederlands."
                ),
            },
            {"role": "user", "content": message},
        ],
        stream=False,
    )
    return response.choices[0].message.content