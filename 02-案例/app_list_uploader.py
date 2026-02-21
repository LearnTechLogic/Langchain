"""
基于StreamLit完成web网页上传服务

Streamlit: 当web元素发生变化，则代码重新执行一遍
"""
import time

import streamlit as st
from konwledge_base import KnowledgeBaseService

st.title("知识库更新服务")

uploader_file = st.file_uploader(
    "请上传TXT文件",
    type=["txt"],
    accept_multiple_files=False,    # False表示仅接受一个文件的上传
)
if "service" not in st.session_state:
    st.session_state["service"] = KnowledgeBaseService()

if uploader_file is not None:
    file_name = uploader_file.name
    file_type = uploader_file.type
    file_size = uploader_file.size / 1024   # KB

    st.subheader(f"文件名: {file_name}")
    st.write(f"文件类型: {file_type} | 文件大小: {file_size:.2f}KB")

    # getvalue -> bytes -> decode('utf_8')
    text = uploader_file.getvalue().decode("utf-8")    # 获取上传文件的内容

    with st.spinner("载入知识库中..."):
        time.sleep(1)
        result = st.session_state["service"].upload_by_str(text, file_name)
        st.write(result)