import gradio as gr
from pdf_processing import pdf_bot_chatbot, pdf_chatbot_response
from llm_setup import conversation_chain, qa_chain
from vector_db_setup import vectorstore

# Gradio 인터페이스 구성
with gr.Blocks() as app:
    # PDF 요약 탭
    with gr.Tab("PDF 문서 요약봇"):
        pdf_input = gr.File(label="PDF 파일 업로드")
        summary_output = gr.Textbox(label="PDF 요약", interactive=False)
        pdf_summary_button = gr.Button("문서 요약", variant="primary")

        pdf_summary_button.click(
            fn=pdf_bot_chatbot,
            inputs=[pdf_input],
            outputs=[summary_output]
        )

    # PDF 기반 챗봇 탭
    with gr.Tab("PDF 기반 챗봇"):
        pdf_input = gr.File(label="PDF 파일 업로드")
        user_input = gr.Textbox(placeholder="질문 입력", lines=1)
        chatbot_output = gr.Chatbot(value=[[None, "### 안녕하세요, 질문을 입력해주세요."]])

        chatbot_button = gr.Button("보내기")
        chatbot_button.click(
            fn=pdf_chatbot_response,
            inputs=[pdf_input, user_input],
            outputs=[chatbot_output]
        )

    # 대화형 강의 계획서 추천 탭
    with gr.Tab("대화형 강의 계획서 추천"):
        school = gr.Textbox(label="대학교")
        department = gr.Textbox(label="학과")
        year = gr.Textbox(label="학년")
        save_button = gr.Button("저장")
        user_info_output = gr.Textbox(label="저장된 정보", interactive=False)

        save_button.click(
            fn=lambda s, d, y: f"{s}, {d}, {y}",
            inputs=[school, department, year],
            outputs=[user_info_output]
        )

app.launch(debug=True)
