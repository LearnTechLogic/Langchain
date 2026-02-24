from abc import ABC, abstractmethod
from typing import Optional
from langchain_core.embeddings import Embeddings
# from langchain_community.chat_models.tongyi import BaseChatModel
# from langchain_community.embeddings import DashScopeEmbeddings
# from langchain_community.chat_models.tongyi import ChatTongyi
from utils.config_handler import rag_conf
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_ollama.chat_models import BaseChatModel
from langchain_ollama.chat_models import ChatOllama


class BaseModelFactory(ABC):
    @abstractmethod
    def generator(self) -> Optional[Embeddings | BaseChatModel]:
        pass


class ChatModelFactory(BaseModelFactory):
    def generator(self) -> Optional[Embeddings | BaseChatModel]:
        return ChatOllama(model=rag_conf["chat_model_name"])
        # return ChatTongyi(model=rag_conf["chat_model_name"])


class EmbeddingsFactory(BaseModelFactory):
    def generator(self) -> Optional[Embeddings | BaseChatModel]:
        return OllamaEmbeddings(model=rag_conf["embedding_model_name"])
        # return DashScopeEmbeddings(model=rag_conf["embedding_model_name"])


chat_model = ChatModelFactory().generator()
embed_model = EmbeddingsFactory().generator()
