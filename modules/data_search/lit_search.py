# Literature Search & Data Retrieval Module for BioMCP-Hub

import requests
import os
from fastapi import FastAPI, HTTPException, Query
from typing import Dict

app = FastAPI(title="BioMCP-Hub Literature Search", description="Retrieve literature from bioRxiv, medRxiv, and PubMed", version="1.0")

# Configuration
PUBMED_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
BIOARXIV_API_URL = "https://api.biorxiv.org/covid19"
MEDRXIV_API_URL = "https://api.medrxiv.org/covid19"

@app.get("/search/pubmed")
def search_pubmed(query: str = Query(..., description="Search query for PubMed"), max_results: int = 10):
    """Search PubMed for articles matching the query."""
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }
    response = requests.get(PUBMED_API_URL, params=params)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="PubMed API request failed")
    return response.json()

@app.get("/fetch/pubmed")
def fetch_pubmed(pmid: str = Query(..., description="PubMed article ID (PMID)")):
    """Fetch full text or abstract from PubMed using PMID."""
    params = {
        "db": "pubmed",
        "id": pmid,
        "retmode": "text",
        "rettype": "abstract"
    }
    response = requests.get(PUBMED_FETCH_URL, params=params)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="PubMed fetch request failed")
    return {"pmid": pmid, "abstract": response.text}

@app.get("/search/biorxiv")
def search_biorxiv(query: str = Query(..., description="Search query for bioRxiv")):
    """Search bioRxiv for preprints matching the query."""
    response = requests.get(f"{BIOARXIV_API_URL}/{query}")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="bioRxiv API request failed")
    return response.json()

@app.get("/search/medrxiv")
def search_medrxiv(query: str = Query(..., description="Search query for medRxiv")):
    """Search medRxiv for preprints matching the query."""
    response = requests.get(f"{MEDRXIV_API_URL}/{query}")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="medRxiv API request failed")
    return response.json()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5050, log_level="info")
