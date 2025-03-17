✅ **已生成 BioMCP-Hub 的序列比对模块 (`sequence_alignment.py`)**，支持：
- **BLAST 比对**（对接 NCBI BLAST 数据库）
- **Clustal Omega**（进行多序列比对）

### **🔹 运行方式**
```sh
uvicorn sequence_alignment:app --host 0.0.0.0 --port 5060 --reload
```
你可以在浏览器访问：
- 📜 `http://localhost:5060/docs` （API 文档）
- 🚀 `POST /align/blast` **(上传序列文件，进行 BLAST 比对)**
- 🔄 `POST /align/clustalo` **(上传 FASTA 文件，进行 Clustal Omega 比对)**

**下一步：** 需要 **增加更多比对工具（如 MAFFT, MUSCLE）** 或 **优化比对参数支持** 🚀
