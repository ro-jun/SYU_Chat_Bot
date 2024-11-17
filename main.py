from llm_setup import llm
from vector_db_setup import vectorstore
from qa_setup import qa_chain
from gradio_ui import app

def main():
    # 초기화 확인 메시지 출력
    print("===== SYU_CHAT_BOT 초기화 중 =====")
    print(f"LLM 설정 완료: {llm}")
    print(f"벡터 데이터베이스 설정 완료: {vectorstore}")
    print(f"Q&A 체인 설정 완료: {qa_chain}")

    # Gradio UI 실행
    app.launch(debug=True)

if __name__ == "__main__":
    main()
