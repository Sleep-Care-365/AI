from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Sleep Care 365 AI Engine",
    description="RAG(Retrieval-Augmented Generation) 기반 맞춤형 수면 코칭 API 서버",
)

# 프론트엔드와 연동을 위한 CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 데이터 규격 정의
class QueryRequest(BaseModel):
    user_id: str
    question: str


@app.get("/")
def read_root():
    return {"message": "Sleep Care 365 RAG AI Engine is running v1.0.0"}


@app.post("/api/ai/coach")
def rag_sleep_coaching(request: QueryRequest):
    """
    RAG 아키텍처 파이프라인 (시연 및 기록용 구조)
    """
    # 1. Retrieval (검색): 사용자의 질문 데이터와 관련된 수면 의학 지식 DB 조회 (가상 가동)
    mock_retrieved_docs = f"[{request.question}] 관련 수면 위생 지식: 규칙적인 입면 시간 유지 및 블루라이트 차단 필요."

    # 2. Prompt Engineering & Augmented (증강): 검색된 지식을 프롬프트에 주입
    system_prompt = f"당신은 전문 수면 코치입니다. 다음 참고 문헌을 바탕으로 답변하세요: {mock_retrieved_docs}"

    # 3. Generation (생성): LLM 모델이 맞춤형 답변 생성 (시연용 가짜 응답)
    ai_response = (
        f"안녕하세요, {request.user_id}님. 질문하신 내용에 대해 RAG 분석을 진행했습니다. "
        "분석 결과, 현재 수면 효율을 높이기 위해 스마트폰 사용을 줄이고 일정한 수면 루틴을 가져가는 것을 추천합니다."
    )

    return {
        "status": "success",
        "retrieved_context": mock_retrieved_docs,
        "ai_answer": ai_response,
    }
