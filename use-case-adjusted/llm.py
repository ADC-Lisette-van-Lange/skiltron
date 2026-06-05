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
                    "Schrijf een professioneel ambtelijk memo op basis van de instructies en data. "
                    "Gebruik duidelijke koppen (beginnen met ##), alinea's en een heldere structuur. "
                    "Schrijf in het Nederlands in een formele ambtelijke stijl. "
                    "Begin het memo met een korte inleiding, verwerk de data in de tekst en sluit af met een conclusie of aanbeveling. "
                    "Gebruik **vetgedrukte tekst** voor belangrijke begrippen. "
                    "Gebruik geen markdown-tabel — gebruik gewone tekst of opsommingen. "
                    "Begin NIET met 'MEMO' als koptitel of eerste regel — dat wordt automatisch toegevoegd door het systeem. "
                    "Begin direct met de inhoud, bijvoorbeeld een inleidende alinea of de eerste kop."
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