from fastapi import APIRouter, UploadFile, File, HTTPException
from app.api.models import UploadResponse, ProfileResult

router = APIRouter(prefix="/api")

@router.post("/upload", response_model=UploadResponse)
async def upload_file(file: UploadFile = File(...)):
    return {"status": "accepted", "message": "File ontvangen"}

@router.get("/results/{job_id}", response_model=ProfileResult)
async def get_results(job_id: str):
    raise HTTPException(status_code=404, detail="Resultaat niet gevonden")
