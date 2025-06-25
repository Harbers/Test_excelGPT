import pandas as pd
from app.config import config

def read_input(path: str) -> pd.DataFrame:
    df = pd.read_excel(path) if path.endswith(".xlsx") else pd.read_csv(path)
    required = {"Bedrijfsnaam", "LinkedIn-URL"}
    if not required.issubset(df.columns):
        raise ValueError(f"Verwachte kolommen missen: {required - set(df.columns)}")
    return df

def write_output(results: dict, path: str):
    out = []
    for r in results:
        out.append({
            "Functie": r["functie"],
            "Naam": r["naam"],
            "LinkedIn-URL": r["linkedin_url"],
        })
    df = pd.DataFrame(out)
    df.to_excel(path, index=False)
