# MCP Hub - Core API for BioMCP-Hub (FastAPI Version)

import os
import json
import mcp
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any

app = FastAPI(title="BioMCP-Hub API", description="MCP-based Bioinformatics Platform", version="1.0")

# Load configuration
CONFIG = {
    "port": int(os.getenv("MCP_HUB_PORT", 5000)),
    "modules_dir": "../modules"
}

# Initialize MCP Hub
hub = mcp.Hub(name="BioMCP-Hub")

def load_modules():
    """Scan and load available MCP modules."""
    modules_path = os.path.abspath(CONFIG["modules_dir"])
    hub.scan_modules(modules_path)
    print(f"Loaded MCP modules from {modules_path}")

class RunRequest(BaseModel):
    module: str
    params: Dict[str, Any] = {}

@app.get("/")
def index():
    return {"message": "BioMCP-Hub is running", "status": "OK"}

@app.get("/modules")
def list_modules():
    """List all registered MCP modules."""
    return hub.list_modules()

@app.post("/run")
def run_module(request: RunRequest):
    """Run a specified MCP module with given parameters."""
    module_name = request.module
    params = request.params
    
    if not module_name:
        raise HTTPException(status_code=400, detail="Module name is required")
    
    response = hub.execute(module_name, params)
    return response

if __name__ == "__main__":
    load_modules()
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=CONFIG["port"], log_level="info")
