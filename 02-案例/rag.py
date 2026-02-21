from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableWithMessageHistory, RunnableLambda
from langchain_core.documents import Document
from vector_stores import VectorStoreService
from langchain_ollama.embeddings import OllamaEmbeddings
import config_data as config
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_ollama.chat_models import ChatOllama
from file_history_store import get_history



class RagService(object):
    def __init__(self):
        self.vector_service = VectorStoreService(
            embedding=OllamaEmbeddings(model=config.embedding_name),
        )

        self.prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", "以我提供的已知参考资料为主，"
                 "简洁和专业的回答用户问题。参考资料:{context}"),
                ("system", "并且我提供用户的对话历史记录，如下:"),
                MessagesPlaceholder("history"),
                ("user", "请回答用户提问:{input}"),
            ]
        )

        self.chat_model = ChatOllama(model=config.chat_model_name)

        self.chain = self.__get_chain()

    def __get_chain(self):
        retriever = self.vector_service.get_retriever()

        def format_document(docs: list[Document]):
            if not docs:
                return "无相关参考资料"
            formatted_str = ""
            for doc in docs:
                formatted_str += f"文档片段:{doc.page_content}\n文档元数据:{doc.metadata}\n\n"
            return formatted_str

        def print_prompt(prompt):
            print("-" * 20)
            print(prompt)
            print("-" * 20 + "\n")
            return prompt

        def format_for_retriever(value: dict) -> str:
            return value["input"]

        def format_for_prompt_template(value):
            new_value = {}
            new_value["input"] = value["input"]["input"]
            new_value["history"] = value["input"]["history"]
            new_value["context"] = value["context"]
            return new_value

        chain = (
            {
                "input": RunnablePassthrough(),
                "context":  RunnableLambda(format_for_retriever) | retriever | format_document
            } | RunnableLambda(format_for_prompt_template) | self.prompt_template | print_prompt | self.chat_model | StrOutputParser()
        )

        conversation_chain = RunnableWithMessageHistory(
            chain,
            get_history,
            input_messages_key="input",
            history_messages_key="history",
        )
        return conversation_chain

if __name__ == '__main__':
    session_config = {
        "configurable": {
            "session_id": "user_001"
        }
    }
    rag_service = RagService()
    res = rag_service.chain.invoke({"input": "春天穿什么颜色的衣服"}, session_config)
    print(res)