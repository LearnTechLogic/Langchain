"""
知识库
"""
import os
import config_data as config
import hashlib
from langchain_chroma import Chroma
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from datetime import datetime


def check_md5(md5_str: str):
    if not os.path.exists(config.md5_path):
        # md5未被处理过
        open(config.md5_path, 'w', encoding='utf-8').close()
        return False
    else:
        for line in open(config.md5_path, 'r', encoding='utf-8').readlines():
            line = line.strip() # 处理字符串前后的空格和回车
            if line == md5_str:
                return True
        return False
def save_md5(md5_str: str):
    with open(config.md5_path, 'a', encoding='utf-8') as f:
        f.write(md5_str + '\n')

def get_string_md5(input_str: str, encoding='utf-8'):
    # 将字符串转换为bytes字节数组
    str_bytes = input_str.encode(encoding = encoding)

    # 创建md5对象
    md5_obj = hashlib.md5()
    md5_obj.update(str_bytes)
    md5_hex = md5_obj.hexdigest()
    return md5_hex

class KnowledgeBaseService(object):
    def __init__(self):
        # 如果文件夹不存在，则创建，如果存在，则跳过
        os.makedirs(config.persist_directory, exist_ok=True)
        self.chroma = Chroma(
            collection_name=config.collection_name, # 数据库表名
            embedding_function=OllamaEmbeddings(model=config.embedding_name),
            persist_directory=config.persist_directory  # 数据库文件目录
        )  # 向量存储的实例Chroma向量数据库对象
        self.spliter = RecursiveCharacterTextSplitter(
            chunk_size=config.chunk_size,    # 分割后的文本段最大长度
            chunk_overlap=config.chunk_overlap, # 连续文本段之间的字符重叠数量
            separators=config.separators,   # 自然段落划分的符号
            length_function=len  # 使用python自带的len函数长度统计的依据
        ) # 文本分割的对象

    def upload_by_str(self, data: str, filename):
        # 将传入的字符串，进行向量化，存入向量数据库中
        md5_hex = get_string_md5(data)
        if check_md5(md5_hex):
            return "【跳过】内容已经存在知识库中"

        if len(data) > config.max_split_char_number:
            # 如果字符串长度超过1000，则进行分割
            knowledge_chunks: list[str] = self.spliter.split_text(data)
        else:
            knowledge_chunks = [data]

        metadata = {
            "source": filename,
            "create_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "operator": "小赵"
        }

        self.chroma.add_texts(
            texts=knowledge_chunks,
            # metadatas=[metadata] * len(knowledge_chunks),
            metadatas=[metadata for _ in knowledge_chunks]
        )

        save_md5(md5_hex)

        return "【成功】内容已经成功载入向量库"



if __name__ == '__main__':
    service = KnowledgeBaseService()
    r = service.upload_by_str("""
    1. 创建一个名为“my_file.txt”的文件，并写入以下内容：
    ```
    Hello, World!908
    ```
    2. 打开“my_file.txt”文件并读取内容。
    3. 将读取到的内容打印到控制台。
    """, "testfile")
    print(r)
