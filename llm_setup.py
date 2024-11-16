from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory, ConversationSummaryBufferMemory
from langchain.chains import ConversationalRetrievalChain, ConversationChain
from vector_db_setup import vectorstore
from config import os

# LLM과 메모리 초기화
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)
memory = ConversationBufferMemory()
conversation_chain = ConversationChain(llm=llm, memory=memory)

# 질의응답 체인 설정
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})
qa_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever)
