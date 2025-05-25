# api/main.py
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
import os
from typing import List

app = FastAPI()

# Enable CORS (allows requests from any domain)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load student data from JSON
def load_student_data():
    json_path = os.path.join(os.path.dirname(__file__), 'students.json')
    with open(json_path, 'r') as file:
        students = json.load(file)
    return {student['name']: student['mark'] for student in students}

students = load_student_data()

@app.get("/api")
async def get_marks(names: List[str] = Query(...)):
    marks = []
    for name in names:
        if name in students:
            marks.append(students[name])
        else:
            marks.append(None)  # Return None if name not found
    return {"marks": marks}
