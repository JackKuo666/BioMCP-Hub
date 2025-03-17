✅ **BioMCP-Hub 的 Docker Compose 配置 (`docker-compose.yml`)**，支持：
- **MCP Hub 主服务**（`5000` 端口）
- **序列比对服务**（`5060` 端口）
- **基因组分析服务**（`5070` 端口）
- **文献搜索服务**（`5050` 端口）
- **数据可视化服务**（`5080` 端口）

### **🔹 运行方式**
```sh
docker-compose up -d
```
你可以查看所有运行中的容器：
```sh
docker ps
```
或者停止所有服务：
```sh
docker-compose down
```

**下一步：** 需要 **Kubernetes (K8s) 部署支持**，或者 **优化 Docker 镜像（减少体积）**🚀
