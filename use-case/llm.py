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