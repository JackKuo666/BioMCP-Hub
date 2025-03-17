✅ ** BioMCP-Hub 的基因组分析模块 (`genome_analysis.py`)**，支持：
- **基因组组装**（使用 **SPAdes** 进行 de novo 组装）
- **基因组注释**（使用 **Prokka** 进行基因功能注释）
- **变异检测**（使用 **bcftools** 进行突变检测）

### **🔹 运行方式**
```sh
uvicorn genome_analysis:app --host 0.0.0.0 --port 5070 --reload
```
你可以在浏览器访问：
- 📜 `http://localhost:5070/docs` （API 文档）
- 🧬 `POST /genome/assemble` **(上传 FASTA，进行基因组组装)**
- 🔬 `POST /genome/annotate` **(上传基因组，进行注释)**
- 🧬 `POST /genome/variant_call` **(上传 BAM/参考基因组，进行变异检测)**

**下一步：** 需要 **扩展更多基因组分析工具（如 PlasmidFinder, EggNOG）** 或 **优化结果格式输出**🚀
