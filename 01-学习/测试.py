# from openai import OpenAI
# client = OpenAI(
#     base_url="http://localhost:11434/v1",
#     api_key="ollama_key",
# )
# response = client.chat.completions.create(
#     model="qwen3:8b",
#     messages=[
#         {"role": "system", "content": "你是一个Python专家."},
#         {"role": "assistant", "content": "我是一个Python专家。请问有什么可以帮您？"},
#         {"role": "user", "content": "for循环输出1到5的数字"},
#     ],
#     stream=True,
# )
# for chunk in response:
#     print(chunk.choices[0].delta.content, end="", flush=True)
# from langchain_community.llms.tongyi import Tongyi
# from langchain_ollama import OllamaLLM
# model = OllamaLLM(model="qwen3:8b")
# res = model.invoke(input="for循环输出1到5的数字")
# print(res)
# res = model.stream(input="for循环输出1到5的数字")
# for chunk in res:
#     print(chunk, end="", flush=True)


# from langchain_ollama.chat_models import ChatOllama
# from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
# model = ChatOllama(model="qwen3:4b")
# # messages = [
# #     SystemMessage(content="你是一名来自边塞的诗人"),
# #     HumanMessage(content="给我写一首唐诗"),
# #     AIMessage(content="锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦"),
# #     HumanMessage(content="给予你上一首格式，再来一首"),
# # ]
# messages = [
#     ("system", "你作为一名来自edge的诗人"),
#     ("human", "给我写一首唐诗"),
#     ("ai", "锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦"),
#     ("human", "给予你上一首格式，再来一首"),
# ]
# for chunk in model.stream(input=messages):
#     print(chunk.content, end="", flush=True)


# from langchain_ollama import OllamaEmbeddings
# model = OllamaEmbeddings(model="qwen3-embedding:4b")
# print(model.embed_query("你好"))
# print(model.embed_documents(["你好", "世界"]))

from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
prompt_template = PromptTemplate.from_template("你是一个{role}，请用{language}语言回答：{question}")

prompt_text = prompt_template.format(role="Python专家", language="中文", question="请写一个for循环输出1到5的数字")
model = OllamaLLM(model="qwen3:4b")
res = model.invoke(input=prompt_text)
print(res)