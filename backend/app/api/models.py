from pydantic import BaseModel
from typing import List

class UploadResponse(BaseModel):
    status: str
    message: str

class Person(BaseModel):
    functie: str
    naam: str
    linkedin_url: str

class ProfileResult(BaseModel):
    job_id: str
    profiles: List[Person]
