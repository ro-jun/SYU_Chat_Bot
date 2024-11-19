from core.qa_setup import qa_chain
from gradio_app.user_info import get_user_info

def lecture_plan_chatbot(question):
    """강의 계획서 챗봇: VectorDB를 활용하여 질문에 답변"""
    user_info = get_user_info()

    if not user_info["school"] or not user_info["department"] or not user_info["year"]:
        return [{"role": "assistant", "content": "먼저 내 정보를 입력해주세요."}]
    
    # 사용자 정보 포함한 프롬프트 생성
    user_context = (
        f"사용자는 {user_info['school']} {user_info['year']}학년 {user_info['department']} 학생입니다. "
        "이를 바탕으로 답변해주세요."
    )

    # QA 체인 입력 데이터 생성
    inputs = {
        "question": f"{user_context} {question}",
        "chat_history": []  # 기본적으로 빈 대화 기록 전달
    }

    try:
        response = qa_chain.invoke(inputs)
        return [{"role": "assistant", "content": response["answer"]}]
    except Exception as e:
        return [{"role": "assistant", "content": f"오류가 발생했습니다: {str(e)}"}]
