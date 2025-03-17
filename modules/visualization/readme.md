✅ **BioMCP-Hub 的可视化模块 (`visualization.py`)**，支持：
- **基因表达分析**（生成 **基因表达水平箱线图**）
- **系统发生树**（解析 **Newick 格式** 并生成 **系统发生树**）

### **🔹 运行方式**
```sh
uvicorn visualization:app --host 0.0.0.0 --port 5080 --reload
```
你可以在浏览器访问：
- 📜 `http://localhost:5080/docs` （API 文档）
- 📊 `GET /visualize/gene_expression?data_file=gene_data.csv` **(生成基因表达可视化)**
- 🌿 `GET /visualize/phylogenetic_tree?tree_file=tree.nwk` **(生成系统发生树可视化)**

**下一步：** 需要 **支持更多可视化类型（如 PCA、热图）** 或 **集成前端交互界面**🚀
