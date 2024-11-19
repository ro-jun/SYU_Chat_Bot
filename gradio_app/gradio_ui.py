import gradio as gr
from gradio_app.user_info import save_user_info
from gradio_app.pdf_processing import pdf_bot_chatbot
from gradio_app.samyook_chatbot import samyook_university_chatbot 
from gradio_app.qa_chatbot import lecture_plan_chatbot
from core.prompts import default_prompt

# Gradio UI 구성
with gr.Blocks() as app:
    # 1. 내 정보 입력 탭
    with gr.Tab("내 정보 입력"):
        # 사용자 정보 입력
        school = gr.Textbox(label="대학교")
        department = gr.Textbox(label="학과")
        year = gr.Textbox(label="학년")
        save_button = gr.Button("저장")
        user_info_output = gr.Textbox(label="저장된 정보", interactive=False)

        save_button.click(
            fn=save_user_info,
            inputs=[school, department, year],
            outputs=[user_info_output]
        )

    # 2. PDF 챗봇 (요약형)
    with gr.Tab("PDF 문서 요약봇"):
        pdf_input = gr.File(label="PDF 파일 업로드")
        summary_output = gr.Textbox(label="PDF 요약", interactive=False)
        pdf_summary_button = gr.Button("문서 요약", variant="primary")

        pdf_summary_button.click(
            fn=lambda pdf_file: pdf_bot_chatbot(pdf_file, default_prompt),
            inputs=[pdf_input],
            outputs=[summary_output]
        )

    # 삼육대학교 챗봇 (대화형)
    with gr.Tab("삼육대학교 챗봇"):
        user_input = gr.Textbox(placeholder="질문 입력", lines=1)
        chatbot_output = gr.Chatbot(
            value=[{"role": "assistant", "content": "### 안녕하세요, 삼육대학교 관련 질문을 입력해주세요."}],
            type="messages"
        )

        chatbot_button = gr.Button("보내기")
        chatbot_button.click(
            fn=samyook_university_chatbot,  # 수정된 응답 함수 사용
            inputs=[user_input],
            outputs=[chatbot_output]
        )

    # 4. 강의계획서 챗봇 (대화형)
    with gr.Tab("강의 계획서 챗봇"):
        user_input = gr.Textbox(placeholder="질문 입력", lines=1)
        chatbot_output = gr.Chatbot(
            value=[{"role": "assistant", "content": "### 안녕하세요, 질문을 입력해주세요."}],
            type="messages"
        )

        chatbot_button = gr.Button("보내기")
        chatbot_button.click(
            fn=lecture_plan_chatbot,
            inputs=[user_input],
            outputs=[chatbot_output]
        )

app.launch(debug=True)
