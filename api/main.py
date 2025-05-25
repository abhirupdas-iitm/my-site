from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Fix CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load data - WILL WORK on Vercel
def get_marks():
    with open(os.path.join(os.path.dirname(__file__), 'students.json')) as f:
        data = json.load(f)
    return {item['name']: item['mark'] for item in data}

marks_data = get_marks()

@app.get("/api")
async def marks(names: list = Query(...)):
    return {"marks": [marks_data.get(name) for name in names]}
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
)
