# main.py (업데이트 버전)
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from rag_service import rag_service  # 💡 방금 만든 RAG 서비스 로드

app = FastAPI(
    title="Sleep Care 365 AI Engine",
    description="RAG(Retrieval-Augmented Generation) 기반 맞춤형 수면 코칭 API 서버",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QueryRequest(BaseModel):
    user_id: str
    question: str


@app.get("/")
def read_root():
    return {"message": "Sleep Care 365 RAG AI Engine is running v1.1.0"}


@app.post("/api/ai/coach")
def rag_sleep_coaching(request: QueryRequest):
    # 1. Retrieval 단계 실행
    context = rag_service.retrieve_relevant_context(request.question)

    # 2 & 3. Augment & Generation 단계 실행
    ai_response = rag_service.generate_augmented_response(request.question, context)

    return {
        "status": "success",
        "user_id": request.user_id,
        "retrieved_context": context,
        "ai_answer": ai_response,
    }
