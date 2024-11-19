import pdfplumber
from core.llm_setup import llm
from core.prompts import pdf_summary_prompt
def pdf_bot_chatbot(pdf_file, prompt):
    """
    PDF 파일을 읽어 OpenAI 모델을 통해 요약 생성
    """
    # 파일 업로드 여부 확인
    if pdf_file is None:
        return "파일을 업로드해주세요."

    # PDF 내용 추출
    try:
        with pdfplumber.open(pdf_file) as pdf:
            text = "".join(page.extract_text() for page in pdf.pages if page.extract_text())
    except Exception as e:
        return f"PDF 처리 중 오류가 발생했습니다: {e}"

    # LangChain 기반 LLM 호출
    try:
        response = llm.predict_messages(
            messages=[
                {"role": "system", "content": pdf_summary_prompt},
                {"role": "user", "content": text}
            ]
        )
        return response.content.strip()
    except Exception as e:
        return f"요약 생성 중 오류가 발생했습니다: {e}"

# def pdf_chatbot_response(pdf, user_input, history=None):
#     """
#     PDF 파일을 읽어 대화 기반 응답 생성
#     """
#     # 파일 업로드 여부 확인
#     if pdf is None:
#         return [{"role": "assistant", "content": "파일을 업로드해주세요."}]

#     # PDF 내용 추출
#     try:
#         with pdfplumber.open(pdf) as pdf_reader:
#             text = "".join(page.extract_text() for page in pdf_reader.pages if page.extract_text())
#     except Exception as e:
#         return [{"role": "assistant", "content": f"PDF 처리 중 오류가 발생했습니다: {e}"}]

#     # 기본 대화 이력 설정
#     if history is None:
#         history = []

#     # LangChain 기반 LLM 호출
#     try:
#         messages = history + [{"role": "user", "content": user_input}]
#         response = llm.predict_messages(
#             messages=messages
#         )

#         assistant_reply = response.content.strip()

#         # 대화 이력 업데이트
#         history.append({"role": "user", "content": user_input})
#         history.append({"role": "assistant", "content": assistant_reply})

#         return history
#     except Exception as e:
#         return [{"role": "assistant", "content": f"응답 생성 중 오류가 발생했습니다: {e}"}]
