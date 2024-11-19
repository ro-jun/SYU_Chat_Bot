from core.llm_setup import llm
from core.vector_db_setup import vectorstore
from core.qa_setup import qa_chain
from gradio_app.gradio_ui import app


def initialize_components():
    """
    SYU_CHAT_BOT의 주요 컴포넌트를 초기화합니다.
    """
    print("===== SYU_CHAT_BOT 초기화 =====")
    if llm:
        print("✅ LLM 설정 완료.")
    else:
        print("❌ LLM 설정 실패.")

    if vectorstore:
        print("✅ 벡터 데이터베이스 설정 완료.")
    else:
        print("❌ 벡터 데이터베이스 설정 실패.")

    if qa_chain:
        print("✅ Q&A 체인 설정 완료.")
    else:
        print("❌ Q&A 체인 설정 실패.")
    print("==============================")


def run_gradio():
    """
    Gradio UI를 실행합니다.
    """
    try:
        print("Gradio UI 실행 중...")
        app.launch(debug=True, share=True)
    except KeyboardInterrupt:
        print("Gradio 서버를 종료합니다.")
        app.close()  # 안전하게 종료


def main():
    """
    SYU_CHAT_BOT의 메인 실행 함수.
    """
    initialize_components()
    run_gradio()


if __name__ == "__main__":
    main()
