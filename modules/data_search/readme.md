✅ ** BioMCP-Hub 的文献搜索模块 (`lit_search.py`)**，支持：
- **PubMed** 查询（使用 NCBI API）
- **bioRxiv** 查询（访问 bioRxiv API）
- **medRxiv** 查询（访问 medRxiv API
- **新增 `/fetch/pubmed?pmid=xxxx`** 用于获取 **PubMed 文章摘要/全文**
- **使用 NCBI EFetch API** 自动拉取 **PMID 对应的全文**

### **🔹 运行方式**
```sh
uvicorn lit_search:app --host 0.0.0.0 --port 5050 --reload
```
你可以在浏览器访问：
- `http://localhost:5050/docs` （API 文档）
- 🔍 `http://localhost:5050/search/pubmed?query=CRISPR` （搜索 PubMed）
- 🔍 `http://localhost:5050/search/biorxiv?query=CRISPR` （搜索 bioRxiv）
- 🔍 `http://localhost:5050/search/medrxiv?query=CRISPR` （搜索 medRxiv）
- 📄 `http://localhost:5050/fetch/pubmed?pmid=12345678` **(获取 PMID 文章摘要)**

**下一步：** 需要 **存储文献数据（PostgreSQL/MongoDB）** 或 **扩展更多数据库（如 UniProt, NCBI Gene）** 🚀
