# Genome Analysis Module for BioMCP-Hub

import os
import subprocess
from fastapi import FastAPI, HTTPException, UploadFile, File
from pathlib import Path

app = FastAPI(title="BioMCP-Hub Genome Analysis", description="Perform genome assembly, annotation, and variant calling", version="1.0")

# Configuration
UPLOAD_DIR = "uploads"
GENOME_ASSEMBLER = os.getenv("GENOME_ASSEMBLER", "/usr/bin/spades.py")
VARIANT_CALLER = os.getenv("VARIANT_CALLER", "/usr/bin/bcftools")
GENOME_ANNOTATOR = os.getenv("GENOME_ANNOTATOR", "/usr/bin/prokka")

os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/genome/assemble")
def genome_assembly(fasta: UploadFile = File(...)):
    """Perform genome assembly using SPAdes."""
    fasta_path = Path(UPLOAD_DIR) / fasta.filename
    with open(fasta_path, "wb") as f:
        f.write(fasta.file.read())
    
    output_dir = fasta_path.with_suffix(".assembly")
    assembly_cmd = [GENOME_ASSEMBLER, "-s", str(fasta_path), "-o", str(output_dir)]
    
    try:
        subprocess.run(assembly_cmd, check=True)
        return {"input": fasta.filename, "assembly_output": str(output_dir)}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Genome assembly failed: {str(e)}")

@app.post("/genome/annotate")
def genome_annotation(genome: UploadFile = File(...)):
    """Annotate a genome using Prokka."""
    genome_path = Path(UPLOAD_DIR) / genome.filename
    with open(genome_path, "wb") as f:
        f.write(genome.file.read())
    
    annotation_dir = genome_path.with_suffix(".annotation")
    annotation_cmd = [GENOME_ANNOTATOR, "--outdir", str(annotation_dir), "--prefix", genome_path.stem, str(genome_path)]
    
    try:
        subprocess.run(annotation_cmd, check=True)
        return {"input": genome.filename, "annotation_output": str(annotation_dir)}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Genome annotation failed: {str(e)}")

@app.post("/genome/variant_call")
def variant_calling(bam: UploadFile = File(...), reference: UploadFile = File(...)):
    """Perform variant calling using bcftools."""
    bam_path = Path(UPLOAD_DIR) / bam.filename
    ref_path = Path(UPLOAD_DIR) / reference.filename
    
    with open(bam_path, "wb") as f:
        f.write(bam.file.read())
    with open(ref_path, "wb") as f:
        f.write(reference.file.read())
    
    vcf_output = bam_path.with_suffix(".vcf")
    variant_cmd = [VARIANT_CALLER, "mpileup", "-Ou", "-f", str(ref_path), str(bam_path), "|", VARIANT_CALLER, "call", "-mv", "-o", str(vcf_output)]
    
    try:
        subprocess.run(" ".join(variant_cmd), shell=True, check=True)
        return {"input": bam.filename, "reference": reference.filename, "variant_output": str(vcf_output)}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Variant calling failed: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5070, log_level="info")
