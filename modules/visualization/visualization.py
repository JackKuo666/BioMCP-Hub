# Visualization Module for BioMCP-Hub

import os
import matplotlib.pyplot as plt
import pandas as pd
from fastapi import FastAPI, HTTPException, Query
from pathlib import Path

app = FastAPI(title="BioMCP-Hub Visualization", description="Generate visualizations for biological data", version="1.0")

# Configuration
VISUALIZATION_DIR = "visualizations"
os.makedirs(VISUALIZATION_DIR, exist_ok=True)

@app.get("/visualize/gene_expression")
def plot_gene_expression(data_file: str = Query(..., description="Path to gene expression CSV file")):
    """Generate a boxplot for gene expression data."""
    data_path = Path(data_file)
    if not data_path.exists():
        raise HTTPException(status_code=404, detail="Data file not found")
    
    df = pd.read_csv(data_path)
    if "gene" not in df.columns or "expression" not in df.columns:
        raise HTTPException(status_code=400, detail="Invalid data format. Expecting 'gene' and 'expression' columns.")
    
    plt.figure(figsize=(10, 5))
    df.boxplot(column="expression", by="gene", grid=False)
    plt.xticks(rotation=90)
    plt.title("Gene Expression Levels")
    plt.xlabel("Gene")
    plt.ylabel("Expression Level")
    
    output_path = Path(VISUALIZATION_DIR) / "gene_expression_plot.png"
    plt.savefig(output_path)
    plt.close()
    
    return {"plot": str(output_path)}

@app.get("/visualize/phylogenetic_tree")
def plot_phylogenetic_tree(tree_file: str = Query(..., description="Path to phylogenetic tree file (Newick format)")):
    """Visualize a phylogenetic tree from a Newick file."""
    try:
        from ete3 import Tree, TreeStyle
        tree = Tree(tree_file, format=1)
        ts = TreeStyle()
        ts.show_leaf_name = True
        
        output_path = Path(VISUALIZATION_DIR) / "phylogenetic_tree.png"
        tree.render(str(output_path), tree_style=ts)
        return {"plot": str(output_path)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Phylogenetic tree visualization failed: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5080, log_level="info")
