from core.qa_setup import qa_chain  # Q&A 체인 가져오기

def samyook_university_chatbot(question):
    """
    삼육대학교 관련 질문에 대해 벡터 DB를 사용하여 응답을 생성합니다.
    """
    # 기본 응답
    default_response = "죄송합니다. 삼육대학교에 대한 정보를 찾을 수 없습니다. 다른 질문을 해주세요."

    # 질문을 VectorDB를 통해 처리
    try:
        inputs = {
            "question": f"삼육대학교 관련 정보: {question}",
            "chat_history": []  # 기본적으로 빈 대화 기록
        }
        response = qa_chain.invoke(inputs)

        # 응답이 없으면 기본 응답 반환
        if not response or "answer" not in response:
            return [{"role": "assistant", "content": default_response}]

        # VectorDB에서 검색한 응답 반환
        return [{"role": "assistant", "content": response["answer"]}]
    except Exception as e:
        # 오류 발생 시 기본 응답 반환
        return [{"role": "assistant", "content": f"오류가 발생했습니다: {str(e)}"}]
