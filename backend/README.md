# Backend Excel → LinkedIn GPT

## Installatie (zonder Docker)
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Met Docker
```bash
docker build -t excel-gpt-backend .
docker run -d -p 8000:8000 excel-gpt-backend
```
