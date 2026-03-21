from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

from resume_parser import parse_resume
from analyzer import analyze_resume

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.get("/")
def home():
    return {"message": "AI Resume Analyzer API Running"}


@app.post("/analyze")
async def analyze(resume: UploadFile = File(...), job_description: str = Form(...)):

    print("REQUEST RECEIVED")

    file_path = os.path.join(UPLOAD_FOLDER, resume.filename)
    print("Saving file:", file_path)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)

    print("Parsing resume...")
    resume_text = parse_resume(file_path)
    print("Resume text length:", len(resume_text) if resume_text else 0)

    print("Running analyzer...")
    result = analyze_resume(resume_text, job_description)

    print("Result:", result)

    return result
