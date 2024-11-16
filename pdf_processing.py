from PyPDF2 import PdfReader
import openai
from config import os

# PDF 파일 요약 함수
def pdf_bot_chatbot(pdf_file, prompt):
    reader = PdfReader(pdf_file.name)
    text = "".join(page.extract_text() for page in reader.pages)

    # GPT-4로 요약 생성
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": f'''
            Please follow the format of {prompt}
            Please always answer in Korean.
            '''},
            {"role": "user", "content": f'''
            Summarize the following text.
            Also write explanations about what you learn each week: {text}
            '''}
        ],
        max_tokens=4096
    )
    return response['choices'][0]['message']['content'].strip()

# PDF 기반 질문 응답 함수
def pdf_chatbot_response(pdf, user_input, summary):
    reader = PdfReader(pdf.name)
    text = "".join(page.extract_text() for page in reader.pages)

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": f'''
            Check if the user's question is included in the {summary}.
            Please always answer in Korean.
            '''},
            {"role": "user", "content": user_input}
        ],
        max_tokens=4096
    )
    return response['choices'][0]['message']['content'].strip()
