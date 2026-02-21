from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_ollama.chat_models import ChatOllama


@tool(description="获取股价，传入股票名称，返回字符串信息")
def get_price(name: str) -> str:
    return f"股票{name}的价格是20元"


@tool(description="获取股票信息，传入股票名称，返回字符串信息")
def get_info(name: str) -> str:
    return f"股票{name}，是一家A股上市公司，专注于IT职业教育。"


agent = create_agent(
    model=ChatOllama(model="qwen3:4b"),
    tools=[get_price, get_info],
    system_prompt="你是一个智能助手，可以回答股票相关问题，记住请告知我思考过程，让我知道你为什么调用某个工具"
)

res = agent.stream(
    {
        "messages": [
            {"role": "user", "content": "传智教育股价多少，并介绍一下"}
        ]
    },
    stream_mode="values"
)

for item in res:
    latest_message = item["messages"][-1]
    print(latest_message)
    if latest_message.content:
        print(type(latest_message).__name__, latest_message.content)
    try:
        if latest_message.tool_calls:
            print(f"工具调用：{[tc['name'] for tc in latest_message.tool_calls]}")
    except AttributeError:
        pass