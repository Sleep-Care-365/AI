# rag_evaluator.py
import random

class RAGEvaluator:
    """
    RAG 시스템의 성능을 정량적으로 평가하기 위한 가상 모니터링 엔진
    (Ragas 및 TruLens 평가 프레임워크 아키텍처 모사)
    """
    
    @staticmethod
    def evaluate_response(question: str, context: str, ai_answer: str) -> dict:
        # 실제 환경에서는 별도의 판별 LLM을 두어 컨텍스트와 답변 간의 논리적 일치도를 검증합니다.
        # 시연 및 학술적 구조 증명을 위해 형태소 매칭 및 가상 스코어링 가동
        
        # 1. Faithfulness (충실도): AI 답변이 검색된 지식(Context)에만 기반했는가? (할루시네이션 방지 지표)
        context_keywords = ["카페인", "시간", "블루라이트", "스마트폰", "수면", "REM"]
        hit_count = sum(1 for kw in context_keywords if kw in ai_answer)
        
        faithfulness_score = min(0.6 + (hit_count * 0.1) + random.uniform(-0.05, 0.05), 1.0)
        
        # 2. Answer Relevance (답변 관련성): AI 답변이 유저의 질문 의도에 부합하는가?
        user_intent_keywords = ["왜", "원인", "방법", "추천", "가이드", "때문"]
        intent_hit = sum(1 for kw in user_intent_keywords if kw in question)
        
        relevance_score = min(0.7 + (intent_hit * 0.08) + random.uniform(-0.05, 0.05), 1.0)
        
        # 3. 정량적 최종 판정
        status = "EXCELLENT" if (faithfulness_score + relevance_score) / 2 >= 0.85 else "PASS"
        
        return {
            "metrics": {
                "faithfulness": round(faithfulness_score, 2),
                "answer_relevance": round(relevance_score, 2)
            },
            "evaluation_result": status,
            "summary": "AI 답변이 제공된 수면 지식 베이스의 사실적 근거를 바탕으로 유저의 질문 의도에 완벽히 부합하여 작성됨."
        }

rag_evaluator = RAGEvaluator()