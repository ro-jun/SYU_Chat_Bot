# prompts.py
default_prompt = '''
학기: 2024-1학기
과목명: 객체지향프로그래밍Ⅰ
담당교수: 김현규
이메일: hgkim@syu.ac.kr
연락처: 01020357553
학점: 3
시수: 1/2
교과목코드: 1000229
교재: 명품자바에센셜 (황기태, 생능출판사, 2020)

수업내용 요약:
- Java언어의 기본 구조와 객체지향 프로그래밍 기법 학습
- 클래스와 객체, 이벤트, 메소드, 상속, 캡슐화, 다형성 등 학습
- 객체지향언어의 특징 이해 및 응용
- 선수과목으로 소프트웨어원리 수강 및 기본적인 알고리즘 작성 능력 요구

주차별 학습계획 요약:
- 1주차: 수업개요 및 환경설정
- 2주차: 데이터타입과 조건문
...

평가비율:
1. 중간고사 %
2. 기말고사 %
3. 출석 20%
4. 기타 15%
...

강의방식: 블렌디드 수업(대면 + 비대면)
'''

pdf_summary_prompt = '''
Please summarize the following PDF file contents in the format provided below:
{default_prompt}
Please always answer in Korean.
'''

qa_chain_prompt = '''
You are a chatbot designed to answer questions using the vector database. Always reply in Korean. When explaining the syllabus, follow this format:
{default_prompt}
'''
