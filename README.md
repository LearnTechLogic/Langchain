# Langchain 学习项目

这是一个基于 Langchain 框架的完整学习项目，涵盖了从基础概念到实际应用的各个方面，包括 RAG（检索增强生成）、智能体开发以及综合项目实践。

## 📚 项目结构

```
D:\Langchain\
├── 01-学习\              # 基础学习模块
│   ├── 数据资料\         # 学习数据集
│   ├── 基础学习.ipynb    # Jupyter Notebook 基础教程
│   └── 测试.py          # 基础功能测试
├── 02-案例\              # 实际应用案例
│   ├── data\            # 案例数据
│   ├── rag.py           # RAG 核心实现
│   ├── app_qa.py        # QA 应用示例
│   ├── vector_stores.py # 向量存储管理
│   └── 其他工具文件...
├── 03-智能体\            # Agent 智能体开发
│   ├── 01智能体初体验.py      # 智能体基础入门
│   ├── 02Agent的stream流式输出.py  # 流式输出实现
│   ├── 03ReAct案例.py    # ReAct 模式案例
│   └── 04middleware中间件.py  # 中间件应用
└── 04-综合项目\          # 综合实战项目
    └── data\            # 项目数据集
```

## 🎯 学习目标

本项目旨在帮助学习者：
- 掌握 Langchain 框架的核心概念和基本用法
- 理解并实现 RAG（检索增强生成）系统
- 开发智能对话代理（Agent）
- 构建完整的 AI 应用项目

## 🔧 技术栈

- **主要框架**: Langchain
- **语言模型**: Ollama (qwen3:4b)
- **向量数据库**: ChromaDB
- **嵌入模型**: qwen3-embedding:4b
- **编程语言**: Python 3.x
- **开发工具**: Jupyter Notebook

## 🚀 快速开始

### 环境准备

1. 安装必要的 Python 包：
```bash
pip install langchain langchain-ollama chromadb
```

2. 确保 Ollama 服务已启动并包含所需模型：
```bash
ollama pull qwen3:4b
ollama pull qwen3-embedding:4b
```

### 运行示例

#### 1. 基础学习
```bash
cd 01-学习
jupyter notebook 基础学习.ipynb
```

#### 2. RAG 案例运行
```bash
cd 02-案例
python rag.py
```

#### 3. 智能体体验
```bash
cd 03-智能体
python 01智能体初体验.py
```

## 📖 详细说明

### 01-学习目录
包含 Langchain 的基础知识学习：
- Python 基础语法复习
- Langchain 核心概念介绍
- 简单的文本处理示例
- 数据加载和预处理方法

### 02-案例目录
实际应用场景的实现：
- **RAG 系统**: 基于向量检索的问答系统
- **知识库管理**: 文档切分、向量化存储
- **对话历史**: 会话状态管理和持久化
- **配置管理**: 系统参数统一配置

### 03-智能体目录
Agent 开发实践：
- 智能体基础创建和调用
- Stream 流式输出处理
- ReAct 模式实现（推理-行动-观察）
- 中间件机制应用

### 04-综合项目
完整的商业级应用：
- 扫地机器人智能客服系统
- 多维度产品咨询（选购、维护、故障处理）
- 基于真实业务场景的知识问答

## ⚙️ 配置说明

项目主要配置位于 `02-案例/config_data.py`：

```python
# 向量数据库配置
collection_name = "rag"
embedding_name = "qwen3-embedding:4b"
persist_directory = "./chroma_db"

# 文本分割参数
chunk_size = 1000
chunk_overlap = 100

# 模型配置
chat_model_name = "qwen3:4b"
similarity_threshold = 1
```

## 📊 数据集说明

### 学习数据
- `Python基础语法.txt`: Python 语法学习资料
- `info.csv`, `stu.csv`: 示例数据文件
- JSON 格式数据文件用于数据处理练习

### 案例数据
- 尺码推荐、洗涤养护、颜色选择相关文本
- 用于构建垂直领域的知识库

### 综合项目数据
- 扫地机器人相关问答（200+条）
- 故障排除指南
- 维护保养手册
- 产品选购指南

## 🛠️ 开发工具

### 推荐开发环境
- **IDE**: VS Code / PyCharm
- **Notebook**: Jupyter Lab
- **版本控制**: Git
- **包管理**: pip / conda

### 调试技巧
1. 使用 logging 记录运行状态
2. 利用 Jupyter 的交互式特性进行调试
3. 查看向量数据库中的实际存储内容
4. 监控模型推理过程和结果

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request 来改进这个学习项目！

### 开发流程
1. Fork 项目仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📝 学习路线建议

### 初学者路径
1. 从 `01-学习` 开始，掌握基础概念
2. 学习 `02-案例` 中的具体实现
3. 尝试修改参数观察效果变化
4. 在 `03-智能体` 中体验高级功能

### 进阶学习
1. 深入理解 RAG 系统架构
2. 自定义 Agent 工具和提示词
3. 优化向量检索效果
4. 构建自己的垂直领域应用

## 📚 参考资源

- [Langchain 官方文档](https://docs.langchain.com/)
- [Ollama 官网](https://ollama.ai/)
- [ChromaDB 文档](https://docs.trychroma.com/)

## 📄 许可证

本项目仅供学习交流使用。

## 🙏 致谢

感谢 Langchain 社区提供的优秀框架和工具，使得 AI 应用开发变得更加简单高效。

---

**注意**: 本项目持续更新中，建议定期查看最新版本获取更多学习内容和案例。