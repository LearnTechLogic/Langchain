from langchain.agents import create_agent
from langchain_ollama.chat_models import ChatOllama
from langchain_core.tools import tool


@tool(description="查询天气")
def get_weather() -> str:
    return "晴天"


agent = create_agent(
    model=ChatOllama(model="qwen3:4b"),
    tools=[get_weather],
    system_prompt="你是一个聊天助手，可以回答用户问题。"
)

res = agent.invoke(
    {
        "messages": [
            {"role": "user", "content": "明天常州的天气如何？"}
        ]
    }
)
print(res)
for msg in res["messages"]:
    print(type(msg).__name__, msg.content)