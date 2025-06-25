from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api import endpoints
import os

app = FastAPI(
    title="Excel → LinkedIn Profiles GPT",
    description="Upload een Excel- of CSV-bestand en krijg LinkedIn-profielinformatie terug",
    version="1.0.0"
)

# Koppel de API-router
app.include_router(endpoints.router)

# Dien statische bestanden zoals openapi.yaml en ai-plugin.json via /.well-known/
well_known_path = os.path.join(os.path.dirname(__file__), "static", ".well-known")
app.mount("/.well-known", StaticFiles(directory=well_known_path), name="well-known")
