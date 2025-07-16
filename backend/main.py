from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import shutil
import os
from uuid import uuid4

from detect import detect_image, detect_video
from db import log_result

app = FastAPI()

# Allow CORS for frontend (e.g., React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Save the uploaded file to disk
        file_ext = os.path.splitext(file.filename)[1]
        filename = f"{uuid4()}{file_ext}"
        file_path = os.path.join(UPLOAD_DIR, filename)

        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        # Detect based on file type
        if file.content_type.startswith("image/"):
            verdict, confidence = detect_image(file_path)
        elif file.content_type.startswith("video/"):
            verdict, confidence = detect_video(file_path)
        else:
            return JSONResponse(status_code=400, content={"error": "Unsupported file type"})

        # Log to MongoDB
        log_result(filename, verdict, confidence)

        return JSONResponse(content={
            "filename": filename,
            "verdict": verdict,
            "confidence": confidence
        })

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
