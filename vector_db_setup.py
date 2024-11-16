import pinecone
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from config import os

# Pinecone 초기화 및 연결 설정
pinecone.init(api_key=os.getenv("PINECONE_API_KEY"), environment=os.getenv("PINECONE_ENV"))
pinecone_client = pinecone.Pinecone()
indexes = pinecone_client.list_indexes()
index_name = indexes[0] if indexes else None

# 벡터 DB와 Embeddings 설정
embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

if index_name:
    # 기존 인덱스를 사용하는 경우
    vectorstore = Pinecone.from_existing_index(index_name, embeddings)
else:
    # 새로운 인덱스를 생성하는 경우
    vectorstore = Pinecone.from_documents([], embeddings, index_name="new_index_name")
