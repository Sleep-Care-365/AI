# 💤 Sleep Care 365 - AI Engine (RAG)

AI 기반 개인 맞춤형 수면 웰니스 솔루션 **'Sleep Care 365'**의 RAG 기반 인공지능 분석 인프라 리포지토리입니다.

## 🚀 Key Architecture: RAG (Retrieval-Augmented Generation)

본 AI 엔진은 단순 LLM의 할루시네이션(환각 현상)을 방지하고, 검증된 수면 의학 데이터 및 사용자의 시계열 수면 기록을 기반으로 정확한 코칭을 제공하기 위해 **검색 증강 생성(RAG)** 파이프라인을 채택하였습니다.

1. **Retrieval**: 유저 질의 및 데이터 패턴 분석 -> 벡터화된 수면 가이드 문서 아카이브 조회
2. **Augmentation**: 검색된 수면 도메인 지식을 LLM 프롬프트 Context에 안전하게 주입
3. **Generation**: 정제된 수면 인디케이터 데이터와 지식을 결합한 하이엔드 수면 코칭 가이드 생성

## 🛠 Tech Stack

- **Framework**: Python FastAPI
- **Server Gateway**: Uvicorn
- **AI Pipeline Design**: LangChain, Pydantic v2
- **Environment**: Virtual Environment (`.venv`)

## 🏃‍♂️ How to Run

```bash
# 1. 가상환경 활성화
.venv\Scripts\activate

# 2. 관련 패키지 설치
pip install -r requirements.txt

# 3. 로컬 개발 서버 구동
uvicorn main:app --reload
```

## 🔗 Main API Specification

- Endpoint: POST /api/ai/coach

- nteractive API Docs: http://localhost:8000/docs (Swagger UI)

---

### 4단계: 깃허브 두 번째 Push (커밋 스택 누적)

터미널에서 방금 추가한 신규 아키텍처 파일과 README를 원격 저장소에 반영합니다.

```bash
# 1. 변경 및 추가된 모든 파일 스테이징
git add .

# 2. RAG 아키텍처 세부 모듈화 및 문서화 명시하여 커밋
git commit -m "feat: implement SleepRAGService pipeline and add repository architecture documentation"

# 3. 깃허브로 푸시!
git push origin main
```
