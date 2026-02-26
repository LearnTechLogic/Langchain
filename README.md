# Langchain 学习项目

这是一个基于 Langchain 框架的完整学习项目，涵盖了从基础概念到实际应用的各个方面，包括 RAG（检索增强生成）、智能体开发以及综合项目实践。

> **最新更新**: 项目已集成 Streamlit 前端界面，提供更好的用户体验
> **项目特色**: 商业级扫地机器人智能客服系统，200+条专业问答数据支撑

## 🎯 项目概述

本项目是一套完整的 Langchain 学习和实践体系，从基础概念到商业级应用，循序渐进地引导学习者掌握 AI 应用开发的核心技能。项目特别包含了基于 ReAct 模式的扫地机器人智能客服系统，展示了如何将理论知识转化为实际的商业解决方案。

## 📚 项目结构

```
D:\Langchain\
├── 01-学习\                  # 📖 基础学习模块
│   ├── 数据资料\             # 学习数据集（CSV、JSON、TXT格式）
│   ├── 基础学习.ipynb        # Jupyter Notebook 基础教程
│   └── 测试.py              # 基础功能验证脚本
├── 02-案例\                  # 🧪 实际应用案例
│   ├── data\                # 案例训练数据
│   ├── rag.py               # RAG 核心实现（检索增强生成）
│   ├── app_qa.py            # QA 应用示例
│   ├── vector_stores.py     # 向量存储管理
│   ├── config_data.py       # 核心配置文件
│   ├── konwledge_base.py    # 知识库构建模块
│   └── 其他工具文件...      # 辅助工具集合
├── 03-智能体\                # 🤖 Agent 智能体开发
│   ├── 01智能体初体验.py          # 智能体基础入门
│   ├── 02Agent的stream流式输出.py # 流式输出实现
│   ├── 03ReAct案例.py        # ReAct 模式案例（推理-行动-观察）
│   └── 04middleware中间件.py      # 中间件应用与监控
└── 04-综合项目\              # 🏢 商业级综合应用
    ├── agent\               # 🤖 智能体核心模块
    │   ├── tools\           # 自定义工具集合
    │   └── react_agent.py   # ReAct 模式主代理
    ├── config\              # ⚙️ YAML 配置文件
    │   ├── rag.yml          # RAG 配置
    │   ├── agent.yml        # Agent 配置
    │   ├── chroma.yml       # 向量数据库配置
    │   └── prompts.yml      # 提示词配置
    ├── data\                # 📊 项目数据集
    │   ├── external\        # 外部数据源
    │   └── 专业问答文档...   # 200+条扫地机器人问答
    ├── model\               # 🏭 模型工厂模式
    ├── prompts\             # 💬 提示词模板库
    ├── rags\                # 🔍 RAG 服务层
    ├── utils\               # 🛠️ 工具函数库
    │   ├── config_handler.py # 配置处理器
    │   ├── file_handler.py   # 文件操作工具
    │   ├── logger_handler.py # 日志管理系统
    │   ├── path_tool.py      # 路径工具
    │   └── prompt_loader.py  # 提示词加载器
    ├── logs\                # 📋 运行日志
    ├── app.py               # 🖥️ Streamlit 主应用
    └── chroma_db\           # 💾 Chroma 向量数据库
```

## 🎯 学习目标

本项目旨在帮助学习者：
- 📚 **掌握 Langchain 核心概念**：从零开始学习 Langchain 框架的基础组件和设计理念
- 🔍 **深入理解 RAG 系统**：掌握检索增强生成的技术原理和实现方法
- 🤖 **开发智能代理系统**：学习 Agent 开发、ReAct 模式和中间件应用
- 🏢 **构建商业级应用**：通过完整的扫地机器人客服系统实践企业级开发
- 🛠️ **培养工程化思维**：学习模块化设计、配置管理、日志系统等工程实践

## 🔧 技术栈

### 核心框架
- **主要框架**: Langchain 0.3+
- **语言模型**: Ollama (qwen3:4b, qwen3.5:cloud)
- **向量数据库**: ChromaDB (本地持久化存储)
- **嵌入模型**: qwen3-embedding:4b

### 前端技术
- **前端框架**: Streamlit 1.30+
- **用户界面**: 响应式聊天界面
- **交互体验**: 实时流式响应

### 工程化工具
- **配置管理**: YAML 配置文件
- **日志系统**: Python logging 模块
- **依赖管理**: pip / conda
- **开发环境**: Jupyter Notebook, VS Code
- **版本控制**: Git

### 编程语言
- **主要语言**: Python 3.8+
- **核心库**: langchain, langchain-ollama, chromadb

## 🚀 快速开始

### 环境准备

#### 1. Python 环境配置
```bash
# 推荐使用 Python 3.8+
pip install langchain==0.3.0 langchain-ollama==0.1.0 chromadb==0.5.0 streamlit==1.30.0 pyyaml==6.0
```

#### 2. Ollama 模型准备
```bash
# 基础模型（必需）
ollama pull qwen3:4b
ollama pull qwen3-embedding:4b

# 高性能模型（可选）
ollama pull qwen3.5:cloud

# 验证模型安装
ollama list
```

#### 3. 项目初始化
```bash
# 克隆项目
git clone <repository-url>
cd Langchain

# 创建虚拟环境（推荐）
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或 venv\Scripts\activate  # Windows

# 安装依赖
pip install -r requirements.txt  # 如果存在requirements文件
```

### 运行示例

#### 1. 📖 基础学习
```bash
cd 01-学习
jupyter notebook 基础学习.ipynb
# 或者直接运行测试脚本
python 测试.py
```

#### 2. 🧪 RAG 案例演示
```bash
cd 02-案例

# 初始化知识库（首次运行）
python konwledge_base.py

# 运行 RAG 问答系统
python rag.py

# 测试 QA 应用
python app_qa.py
```

#### 3. 🤖 智能体功能体验
```bash
cd 03-智能体

# 基础智能体体验
python 01智能体初体验.py

# 流式输出演示
python 02Agent的stream流式输出.py

# ReAct 模式案例
python 03ReAct案例.py

# 中间件监控功能
python 04middleware中间件.py
```

#### 4. 🏢 商业级应用运行
```bash
cd 04-综合项目

# 启动 Streamlit 前端
streamlit run app.py

# 访问地址
# 浏览器打开: http://localhost:8501

# 查看运行日志
ls logs/
tail -f logs/app.log
```

#### 5. 🛠️ 开发调试模式
```bash
# 启用详细日志
cd 04-综合项目
export LOG_LEVEL=DEBUG  # Linux/Mac
# 或 set LOG_LEVEL=DEBUG  # Windows
streamlit run app.py

# 单元测试
python -m pytest tests/ -v
```

## 📖 详细说明

### 📚 01-学习目录 - 基础入门
包含 Langchain 的基础知识学习，适合零基础学习者：

**核心内容：**
- 🐍 **Python 基础语法复习**: 数据类型、控制结构、函数等
- 🔗 **Langchain 核心概念**: LLM、Prompt、Chain、Agent 等基础组件
- 💬 **文本处理实践**: 提示词工程、文本生成、对话系统
- 📊 **数据处理技能**: CSV、JSON、TXT 文件的加载和预处理
- 🧪 **基础实验验证**: 通过 Jupyter Notebook 交互式学习

**学习建议：**
- 先运行 `基础学习.ipynb` 理解核心概念
- 修改 `测试.py` 观察不同参数的效果
- 重点掌握 Langchain 的基本组件使用

### 🧪 02-案例目录 - 应用实践
实际业务场景的完整实现，展示核心技术应用：

**关键技术点：**
- 🔍 **RAG 系统实现**: 向量检索、语义搜索、上下文增强
- 🗃️ **知识库构建**: 文档切分、向量化存储、相似度匹配
- 💾 **对话状态管理**: 会话历史持久化、上下文维护
- ⚙️ **配置系统**: 参数化配置、环境适配

**核心文件说明：**
- `rag.py`: RAG 核心服务实现
- `konwledge_base.py`: 知识库初始化和管理
- `vector_stores.py`: 向量数据库操作封装
- `config_data.py`: 系统配置参数定义

### 🤖 03-智能体目录 - 高级特性
Agent 智能体开发的完整实践，涵盖前沿技术：

**学习内容：**
- 🤖 **智能体基础**: Agent 创建、工具注册、调用机制
- 🌊 **流式处理**: 实时响应输出、用户体验优化
- 🔄 **ReAct 模式**: 推理-行动-观察循环机制
- 🛡️ **中间件应用**: 请求拦截、监控、日志记录

**技术亮点：**
- 实现了完整的工具调用链路
- 支持复杂业务逻辑处理
- 具备完善的监控和调试能力

### 🏢 04-综合项目 - 商业应用
完整的商业级扫地机器人智能客服系统：

**系统架构：**
- 🖥️ **前端界面**: Streamlit 聊天界面，支持实时交互
- 🧠 **智能核心**: ReAct 模式 Agent，支持多轮对话
- 🔧 **工具生态**: 7个专业工具，覆盖完整业务场景
- 📊 **数据支撑**: 200+条专业问答，真实业务数据
- ⚙️ **配置管理**: YAML 配置驱动，支持灵活部署
- 📋 **日志系统**: 完整运行记录，便于问题追踪

**核心功能：**
- 🛒 **产品咨询**: 选购指南、型号推荐、功能对比
- 🔧 **技术支持**: 故障诊断、维修指导、配件更换
- 🧹 **使用指导**: 操作说明、清洁技巧、日常维护
- 📈 **数据分析**: 使用报告生成、性能分析、趋势预测
- 🌡️ **环境适配**: 地区天气影响、季节性建议

**业务价值：**
- 提升客户服务质量
- 降低人工客服成本
- 7×24小时智能响应
- 个性化精准推荐

## ⚙️ 配置说明

### 🛠️ 基础案例配置
项目主要配置位于 `02-案例/config_data.py`，控制核心行为参数：

```python
# 🗃️ 向量数据库配置
collection_name = "rags"      # ChromaDB 集合名称
embedding_name = "qwen3-embedding:4b"  # 嵌入模型
persist_directory = "./chroma_db"       # 本地存储路径

# ✂️ 文本分割参数
chunk_size = 1000             # 每个文本块大小
chunk_overlap = 100           # 块间重叠字符数
separators = ['\n\n', '\n', ' ', '', '!', '?', ';', ':', ',', '！', '？', '；', '：', '，']

# 🤖 模型配置
chat_model_name = "qwen3:4b"  # 对话模型名称
similarity_threshold = 1      # 检索返回的文档数量

# 👥 会话配置
session_config = {
    "configurable": {
        "session_id": "user_002"  # 用户会话标识
    }
}
```

### ⚙️ 综合项目配置
采用模块化的 YAML 配置文件管理，支持灵活部署：

**RAG 配置** (`04-综合项目/config/rag.yml`)：
```yaml
# 对话模型配置
chat_model_name: qwen3.5:cloud    # 高性能云端模型
# chat_model_name: qwen3:4b       # 本地基础模型

# 嵌入模型配置
embedding_model_name: qwen3-embedding:4b
```

**Agent 配置** (`04-综合项目/config/agent.yml`)：
```yaml
# 外部数据源路径
external_data_path: data/external/records.csv
```

**ChromaDB 配置** (`04-综合项目/config/chroma.yml`)：
```yaml
# 数据库连接配置
database_path: ./chroma_db
collection_name: robot_knowledge
similarity_search_k: 3
```

**提示词配置** (`04-综合项目/config/prompts.yml`)：
```yaml
# 提示词模板路径
main_prompt_path: prompts/main_prompt.txt
rag_summarize_prompt_path: prompts/rag_summarize.txt
report_prompt_path: prompts/report_prompt.txt
```

### 🎛️ 配置最佳实践

**环境区分：**
```bash
# 开发环境
export ENV=development

# 生产环境
export ENV=production
```

**动态切换：**
```python
# 根据环境加载不同配置
if os.getenv('ENV') == 'production':
    config = load_production_config()
else:
    config = load_development_config()
```

**配置验证：**
```python
# 启动时验证配置完整性
validate_configurations()
check_model_availability()
verify_database_connection()
```

## 📊 数据集说明

### 📚 学习数据集
为初学者提供多样化的练习材料：

**结构化数据：**
- `info.csv`: 用户信息表格数据，练习 CSV 处理
- `stu.csv`: 学生信息数据集，包含成绩等字段
- `stu.json`, `stus.json`: JSON 格式学生数据，练习嵌套结构处理
- `stu_json_lines.json`: JSON Lines 格式，逐行处理练习

**文本资料：**
- `Python基础语法.txt`: 详细的 Python 语法参考手册（755行）
- 尺码推荐、洗涤养护、颜色选择等垂直领域文本

### 🧪 案例数据集
构建垂直领域知识库的专业数据：

**业务文档：**
- 尺码推荐指南：服装尺寸选择专业知识
- 洗涤养护手册：纺织品清洗保养规范
- 颜色选择指导：色彩搭配和应用建议

**技术特点：**
- 领域专业性强
- 内容结构化程度高
- 适合构建行业知识库

### 🏢 综合项目数据集
商业级扫地机器人客服系统的丰富数据支撑：

**核心问答库（200+条）：**
- 📄 `扫地机器人100问2.txt`: 基础功能和使用问答
- 📄 `扫拖一体机器人100问.txt`: 高级功能专业解答
- 🛠️ `故障排除.txt` (41KB): 165个常见故障解决方案
- 🔧 `维护保养.txt` (23KB): 日常维护和保养指南
- 🛒 `选购指南.txt` (21KB): 产品选择和购买建议

**外部数据源：**
- `records.csv`: 用户使用记录数据
  - 包含用户ID、居住环境、使用习惯等信息
  - 支持个性化报告生成
  - 真实业务场景模拟

**数据特征：**
- 🎯 **覆盖面广**: 从选购到维护全生命周期
- 📈 **专业性强**: 技术细节和解决方案详尽
- 🔄 **实时更新**: 基于最新产品特性和用户反馈
- 📊 **结构清晰**: 便于知识抽取和向量化处理

## 💡 项目亮点

### 🌟 核心特性
- **📚 完整的学习路径**: 从基础概念到商业应用的系统化学习体系
- **🧪 实用案例驱动**: 基于真实业务场景的技术实现和应用示范
- **🖥️ 现代化交互体验**: Streamlit 前端提供流畅的用户界面
- **🏗️ 模块化架构设计**: 清晰的代码组织，支持灵活扩展和维护
- **⚙️ 丰富的配置选项**: 多种模型支持和参数调优能力

### 🛠️ 工程化最佳实践
- **🔧 配置驱动开发**: YAML 配置文件管理，代码与配置分离
- **📋 完善的日志系统**: 多级别日志记录，便于问题追踪和调试
- **📁 标准化目录结构**: 符合 Python 项目规范的组织方式
- **🧩 可复用组件设计**: 工具函数库和通用模块，提升开发效率
- **📝 清晰的文档注释**: 详细的代码说明和使用指南

### 🔥 技术创新点
- **🤖 ReAct 模式应用**: 推理-行动-观察循环机制的实际落地
- **🛡️ 中间件架构**: 请求监控、日志记录、上下文管理一体化
- **📊 多维度数据融合**: 结构化数据与非结构化文本的统一处理
- **📈 智能报告生成**: 基于用户数据的个性化分析报告
- **🌡️ 环境感知能力**: 结合地理位置和天气因素的智能建议

### 🎯 商业价值体现
- **💼 降低客服成本**: 7×24小时智能响应，减少人工投入
- **🚀 提升服务效率**: 秒级响应，精准解答用户问题
- **🎯 个性化体验**: 基于用户画像的定制化服务
- **📊 数据驱动决策**: 用户行为分析和产品优化建议
- **🔄 持续迭代优化**: 基于反馈的智能系统自我完善

## 🛠️ 开发工具

### 💻 推荐开发环境

**IDE 工具：**
- **VS Code**: 推荐插件 - Python、Jupyter、GitLens
- **PyCharm**: Professional 版本支持科学计算
- **Jupyter Lab**: 交互式开发和数据分析

**版本管理：**
- **Git**: 版本控制和协作开发
- **GitHub/GitLab**: 代码托管和 CI/CD

**包管理：**
- **pip**: Python 官方包管理器
- **conda**: 环境管理和依赖解决
- **poetry**: 现代化依赖管理

**模型工具：**
- **Ollama**: 本地大模型管理平台
- **Docker**: 容器化部署（可选）

### 🎯 项目技术特色

**架构优势：**
- **🏗️ 模块化设计**: 高内聚低耦合，便于维护扩展
- **⚙️ 配置驱动**: YAML 配置文件，支持环境隔离
- **📋 日志系统**: 多级别日志，完整运行追踪
- **🖥️ 前端交互**: Streamlit 实时响应，用户体验佳
- **🔄 多模型支持**: 本地/云端模型无缝切换

### 🐛 调试与优化技巧

**开发调试：**
1. **日志跟踪**: 使用不同日志级别定位问题
   ```python
   logger.debug("详细调试信息")
   logger.info("一般运行信息")
   logger.warning("警告信息")
   logger.error("错误信息")
   ```

2. **交互式调试**: Jupyter Notebook 实时验证想法
   ```python
   # 在 notebook 中逐步验证逻辑
   result = my_function(test_input)
   print(f"结果: {result}")
   ```

3. **向量数据库检查**: 验证检索效果
   ```python
   # 查看存储的向量内容
   docs = vector_store.similarity_search("查询词", k=3)
   for doc in docs:
       print(doc.page_content[:100])
   ```

**性能优化：**
4. **模型监控**: 跟踪推理时间和资源消耗
   ```python
   import time
   start_time = time.time()
   result = model.invoke(prompt)
   print(f"耗时: {time.time() - start_time:.2f}秒")
   ```

5. **前端优化**: Streamlit 响应式设计
   ```python
   # 添加加载状态提示
   with st.spinner("智能客服正在思考..."):
       response = agent.execute_stream(user_input)
   ```

6. **配置调优**: 通过配置文件快速测试不同参数
   ```yaml
   # rag.yml
   chat_model_name: qwen3:4b      # 基础性能
   # chat_model_name: qwen3.5:cloud  # 高性能选项
   ```

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request 来改进这个学习项目！我们鼓励社区参与和知识分享。

### 🎯 贡献方向

**技术实现类：**
- 🔧 **新的案例实现**: 垂直领域的 RAG 应用场景
- ⚡ **性能优化**: 检索速度、响应时间、资源利用率提升
- 🛠️ **最佳实践分享**: 代码重构、架构改进、设计模式应用

**文档完善类：**
- 📚 **技术教程**: 详细的操作指南和原理说明
- 📖 **API 文档**: 函数接口和使用方法说明
- 🎨 **示例代码**: 清晰易懂的代码样例

**功能增强类：**
- 🐛 **错误修复**: Bug 修复和稳定性改进
- ✨ **功能增强**: 新特性开发和现有功能完善
- 🤖 **模型集成**: 支持更多大语言模型和嵌入模型

### 🔄 开发流程

1. **Fork 项目**
   ```bash
   # Fork 到你的 GitHub 账户
   git clone https://github.com/your-username/Langchain.git
   cd Langchain
   ```

2. **创建功能分支**
   ```bash
   git checkout -b feature/amazing-feature
   # 或者修复分支
   git checkout -b fix/important-bug
   ```

3. **开发和测试**
   ```bash
   # 确保代码质量
   python -m pytest tests/ -v
   
   # 检查代码风格
   flake8 .
   black .
   ```

4. **提交更改**
   ```bash
   git add .
   git commit -m "feat: 添加令人惊叹的新功能"
   git push origin feature/amazing-feature
   ```

5. **发起 Pull Request**
   - 在 GitHub 上创建 PR
   - 详细描述变更内容和解决的问题
   - 关联相关的 Issue

### 📋 贡献规范

**代码规范：**
- 遵循 PEP 8 Python 编码规范
- 添加必要的类型注解
- 编写清晰的函数和类文档字符串
- 保持代码简洁和可读性

**提交信息格式：**
```
type(scope): description

详细说明变更内容和影响

Fixes #123
```

**类型说明：**
- `feat`: 新功能
- `fix`: Bug 修复
- `docs`: 文档更新
- `style`: 代码格式调整
- `refactor`: 代码重构
- `test`: 测试相关
- `chore`: 构建过程或辅助工具变动

## 📝 学习路线建议

### 初学者路径
1. 从 `01-学习` 开始，掌握基础概念
2. 学习 `02-案例` 中的具体实现
3. 尝试修改参数观察效果变化
4. 在 `03-智能体` 中体验高级功能
5. 运行 `04-综合项目` 体验完整应用

### 进阶学习
1. 深入理解 RAG 系统架构和优化策略
2. 自定义 Agent 工具和提示词工程
3. 优化向量检索效果和相似度算法
4. 构建自己的垂直领域应用
5. 学习配置管理和部署最佳实践

### 专家级挑战
1. 实现多 Agent 协作系统
2. 集成外部 API 和数据库
3. 设计复杂的业务逻辑处理
4. 性能优化和监控告警
5. 企业级部署和运维

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

**项目状态**: ✅ 稳定可用 | 🔄 持续更新 | 📈 功能增强中