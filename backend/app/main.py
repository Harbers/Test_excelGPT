from fastapi import FastAPI
from app.api import endpoints

app = FastAPI(title="Excel → LinkedIn Profiles GPT")
app.include_router(endpoints.router)
