import pandas as pd
from pathlib import Path

CSV_PATH = r"C:\Users\ThomasBerseeADC\Downloads\019e928f-fc30-7c9f-8fd0-b74210a6d378.csv"

_df = None

def load():
    global _df
    _df = pd.read_csv(CSV_PATH, dtype=str).fillna("")
    _df["_routing"] = _df["klachtcategorie"].map(get_routing).fillna("Nader te bepalen")

def get_routing(categorie: str) -> str:
    mapping = {
        "Geluid": "Afdeling Milieu & Leefomgeving",
        "Slaapverstoring": "Afdeling Milieu & Leefomgeving",
        "Geur / luchtkwaliteit": "Afdeling Milieu & Leefomgeving",
        "Meetwaarde / piekgeluid": "Afdeling Milieu & Leefomgeving",
        "Baangebruik": "Bewoners Aanspreekpunt Schiphol (BAS)",
        "Structurele hinder": "Beleidsadviseur Schiphol",
        "Service / luchthavenervaring": "Schiphol Customer Service",
    }
    return mapping.get(categorie, "Nader te bepalen")

def get_conceptantwoord(row: dict) -> str:
    naam = row.get("melder_naam") or "melder"
    categorie = row.get("klachtcategorie", "")
    templates = {
        "Geluid": f"Geachte {naam},\n\nDank voor uw melding over geluidsoverlast rondom Schiphol. Wij hebben uw melding geregistreerd en doorgezet naar de afdeling Milieu & Leefomgeving. U ontvangt zo spoedig mogelijk een reactie.\n\nMet vriendelijke groet,\nGemeente Aalsmeer",
        "Slaapverstoring": f"Geachte {naam},\n\nDank voor uw melding. Slaapverstoring door vliegverkeer is een serieus aandachtspunt voor de gemeente. Uw melding is geregistreerd en wordt meegenomen in onze periodieke rapportage aan het Rijk.\n\nMet vriendelijke groet,\nGemeente Aalsmeer",
        "Geur / luchtkwaliteit": f"Geachte {naam},\n\nDank voor uw melding over geur- en luchtkwaliteitsproblemen. Wij nemen dit mee in onze monitoring en hebben uw melding doorgezet naar de afdeling Milieu.\n\nMet vriendelijke groet,\nGemeente Aalsmeer",
        "Baangebruik": f"Geachte {naam},\n\nDank voor uw vraag over baangebruik. Voor vragen en meldingen over specifiek baangebruik kunt u terecht bij het Bewoners Aanspreekpunt Schiphol (BAS). Wij zetten uw melding daarheen door.\n\nMet vriendelijke groet,\nGemeente Aalsmeer",
        "Structurele hinder": f"Geachte {naam},\n\nDank voor uw melding over structurele hinder. Dit soort signalen zijn waardevol voor onze bestuurlijke lobby richting het Rijk en Schiphol. Uw melding is geregistreerd.\n\nMet vriendelijke groet,\nGemeente Aalsmeer",
        "Meetwaarde / piekgeluid": f"Geachte {naam},\n\nDank voor uw melding inclusief meetgegevens. Wij verwerken uw geluidsmeting in onze registratie. De afdeling Milieu neemt uw melding in behandeling.\n\nMet vriendelijke groet,\nGemeente Aalsmeer",
    }
    return templates.get(categorie, f"Geachte {naam},\n\nDank voor uw melding. Wij hebben deze geregistreerd en nemen zo spoedig mogelijk contact met u op.\n\nMet vriendelijke groet,\nGemeente Aalsmeer")

def all_meldingen():
    return _df.to_dict(orient="records")

def get_melding(melding_id: str):
    rows = _df[_df["melding_id"] == melding_id]
    if rows.empty:
        return None
    return rows.iloc[0].to_dict()

def dashboard_stats():
    totaal = len(_df)
    open_ = len(_df[_df["status"].isin(["Nieuw", "In behandeling"])])
    gesloten = len(_df[_df["status"] == "Gesloten"])
    beantwoord = len(_df[_df["status"] == "Beantwoord"])

    # Counts per woonplaats — inclusief < 5 (foute versie)
    per_woonplaats = (
        _df[_df["woonplaats"] != ""]
        .groupby("woonplaats")
        .size()
        .reset_index(name="aantal")
        .sort_values("aantal", ascending=False)
        .head(10)
        .to_dict(orient="records")
    )

    # Counts per categorie
    per_categorie = (
        _df[_df["klachtcategorie"] != ""]
        .groupby("klachtcategorie")
        .size()
        .reset_index(name="aantal")
        .sort_values("aantal", ascending=False)
        .to_dict(orient="records")
    )

    # Recente meldingen — inclusief naam, email, omschrijving (foute versie)
    recente = _df.head(8)[["melding_id", "datum_melding", "melder_naam", "email", "klachtcategorie", "woonplaats", "omschrijving", "status"]].to_dict(orient="records")

    return {
        "totaal": totaal,
        "open": open_,
        "gesloten": gesloten,
        "beantwoord": beantwoord,
        "per_woonplaats": per_woonplaats,
        "per_categorie": per_categorie,
        "recente": recente,
    }

def add_melding(data: dict):
    global _df
    new_id = f"SIM-{len(_df)+1:04d}"
    new_row = {col: "" for col in _df.columns}
    new_row.update(data)
    new_row["melding_id"] = new_id
    new_row["status"] = "Nieuw"
    new_row["_routing"] = get_routing(data.get("klachtcategorie", ""))
    _df = pd.concat([pd.DataFrame([new_row]), _df], ignore_index=True)
    return new_id
