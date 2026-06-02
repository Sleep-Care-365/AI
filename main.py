# main.py (최종 안정화 버전)
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
from rag_service import rag_service

app = FastAPI(
    title="Sleep Care 365 AI Engine",
    description="RAG(Retrieval-Augmented Generation) 기반 맞춤형 수면 코칭 API 서버",
    version="1.2.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 프론트엔드 입력 데이터 검증 강화
class QueryRequest(BaseModel):
    user_id: str = Field(
        ..., example="user_myeongseong", description="사용자 고유 식별자"
    )
    question: str = Field(
        ...,
        example="최근에 REM 수면 비율이 떨어진 거 같은데 커피 때문일까?",
        description="유저 질의 및 데이터 분석 요청 사항",
    )


@app.get("/health")
def health_check():
    """서버 가동 상태 모니터링을 위한 헬스체크 엔드포인트"""
    return {"status": "healthy", "engine": "RAG_v1.2.0"}


@app.post("/api/ai/coach", status_code=status.HTTP_200_OK)
def rag_sleep_coaching(request: QueryRequest):
    # 유효성 검사 모사
    if not request.user_id or not request.question:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="필수 요청 인자(user_id 또는 question)가 누락되었습니다.",
        )

    try:
        # 1. Retrieval (검색)
        context = rag_service.retrieve_relevant_context(request.question)

        # 2 & 3. Augment & Generation (증강 및 가상 생성)
        ai_response = rag_service.generate_augmented_response(request.question, context)

        # 4. 모니터링을 위한 백엔드 콘솔 로그 출력 (RAG 히트율 기록용)
        print(f"[RAG LOG] User: {request.user_id} | Query: {request.question}")
        print(f"[RAG LOG] Hit Context: {context[:30]}...")

        return {
            "status": "success",
            "metadata": {"algorithm": "RAG-LLM-Augmented", "version": "1.2.0"},
            "data": {
                "user_id": request.user_id,
                "retrieved_knowledge": context,
                "ai_coaching_feedback": ai_response,
            },
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"AI 엔진 내부 구동 중 오류가 발생했습니다: {str(e)}",
        )
