# Sequence Alignment Module for BioMCP-Hub

import os
import subprocess
from fastapi import FastAPI, HTTPException, UploadFile, File
from pathlib import Path

app = FastAPI(title="BioMCP-Hub Sequence Alignment", description="Perform sequence alignment using BLAST and Clustal Omega", version="1.0")

# Configuration
BLAST_DB_PATH = os.getenv("BLAST_DB_PATH", "/usr/local/blast/db")
CLUSTALO_EXEC = os.getenv("CLUSTALO_EXEC", "/usr/bin/clustalo")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/align/blast")
def run_blast(query: UploadFile = File(...)):
    """Perform BLAST sequence alignment."""
    query_path = Path(UPLOAD_DIR) / query.filename
    with open(query_path, "wb") as f:
        f.write(query.file.read())
    
    blast_output = query_path.with_suffix(".blast.txt")
    blast_cmd = [
        "blastn", "-query", str(query_path), "-db", BLAST_DB_PATH, "-out", str(blast_output), "-outfmt", "6"
    ]
    
    try:
        subprocess.run(blast_cmd, check=True)
        return {"query": query.filename, "results": blast_output.read_text()}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"BLAST failed: {str(e)}")

@app.post("/align/clustalo")
def run_clustalo(sequences: UploadFile = File(...)):
    """Perform multiple sequence alignment using Clustal Omega."""
    seq_path = Path(UPLOAD_DIR) / sequences.filename
    with open(seq_path, "wb") as f:
        f.write(sequences.file.read())
    
    output_path = seq_path.with_suffix(".aligned.fasta")
    clustalo_cmd = [CLUSTALO_EXEC, "-i", str(seq_path), "-o", str(output_path), "--force"]
    
    try:
        subprocess.run(clustalo_cmd, check=True)
        return {"input": sequences.filename, "alignment": output_path.read_text()}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Clustal Omega alignment failed: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5060, log_level="info")
