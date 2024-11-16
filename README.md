# SYU_CHAT_BOT
SYU_CHAT_BOT은 강의 계획서 관리와 대화형 강의 계획서 설명을 지원하는 챗봇입니다. PDF 요약, 벡터 데이터베이스 통합, 대화형 사용자 인터페이스 등의 기능을 제공합니다.

---
## 주요 기능
- **챗봇 기능**: 강의 계획서에 대한 질문 및 답변 지원
- **PDF 처리**: 업로드된 PDF 파일에서 내용을 추출하고 요약
- **벡터 데이터베이스 통합**: 질문에 맞는 문서를 검색하고 추천
- **사용자 친화적 UI**: Gradio 기반의 직관적인 웹 인터페이스 제공

---
## 제공 기능
- **PDF 요약**: PDF 파일을 업로드하여 간결한 요약 생성
- **챗봇 대화**: 강의 내용이나 질문에 대해 대화형으로 답변 제공
- **강의 추천**: 입력한 정보에 따라 강의 계획서를 추천

---
## 설치 방법
### 1. 레포지토리 클론
```bash
git clone https://github.com/yourusername/SYU_CHAT_BOT.git
cd SYU_CHAT_BOT
```

### 2. Conda 가상환경 생성
Pyhton 3.11.9 기반 가상환경을 생성하고 활성화합니다.
```bash
conda create -n SYU_CHAT_BOT python=3.11.9
conda activate SYU_CHAT_BOT
```

### 3. 필수 패키지 설치
requirements.txt 파일을 사용하여 모든 의존성을 설치합니다.
```bash
pip install -r requirements.txt
```

### 4. 환경 변수 설정
.env 파일을 생성하고 아래 내용을 추가하세요:
```bash
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENV=your_pinecone_environment
```

---
## 사용 방법
```bash
python gradio_ui.py
```
---
## 프로젝트 구조
```
SYU_CHAT_BOT/
├── config.py             # 환경 변수 설정 파일
├── vector_db_setup.py    # 벡터 데이터베이스 설정 및 초기화
├── llm_setup.py          # 언어 모델(LLM) 및 메모리 설정
├── pdf_processing.py     # PDF 파일 처리 및 요약 기능
├── gradio_ui.py          # Gradio UI 인터페이스 코드
├── prompts.py            # 재사용 가능한 챗봇 프롬프트 저장
├── test.ipynb            # 기능별 테스트용 Jupyter Notebook
└── requirements.txt      # 필수 패키지 목록
```

---
## 필요 요구사항
- 챗봇 기능: 강의 계획서에 대한 질문 및 답변 지원
- Python 3.11.9
- requirements.txt에 나열된 패키지 설치

---
## 감사의 말
- LangChain
- Gradio
- Pinecone
  
---
## 라이선스
이 프로젝트는 MIT 라이선스 하에 제공됩니다.
