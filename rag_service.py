# rag_service.py
import os


class SleepRAGService:
    def __init__(self):
        # 실제 환경이라면 Vector DB(Chroma, Faiss 등)나 임베딩 모델을 여기서 로드합니다.
        # 시연 및 구조 증명을 위해 가상 지식 베이스(Mock Knowledge Base)를 구축합니다.
        self.knowledge_base = [
            {
                "topic": "불면증",
                "content": "카페인 섭취는 입면을 방해하므로 오후 2시 이후에는 제한하는 것이 좋습니다.",
            },
            {
                "topic": "수면 루틴",
                "content": "매일 동일한 시간에 기상하고 취침하는 것은 생체 리듬과 수면 효율을 극대화합니다.",
            },
            {
                "topic": "수면 환경",
                "content": "디바이스의 블루라이트는 멜라토닌 분비를 억제하므로 취침 1시간 전에는 스마트폰 사용을 지양해야 합니다.",
            },
            {
                "topic": "REM 수면",
                "content": "REM 수면은 기억 저장과 감정 조절에 중요하며, 스트레스 수준이 높을 때 비율이 불규칙해집니다.",
            },
        ]

    def retrieve_relevant_context(self, user_question: str) -> str:
        """
        사용자 질문에서 키워드를 추출하여 가상 Vector DB에서 가장 유사도가 높은 컨텍스트를 검색합니다.
        """
        # 실제로는 embedding_vector.similarity_search()가 수행되는 영역입니다.
        # 가볍게 키워드 매칭 방식으로 RAG 검색 로직을 시뮬레이션합니다.
        matched_contexts = []
        for doc in self.knowledge_base:
            if doc["topic"] in user_question or any(
                kw in user_question for kw in ["잠", "수면", "베개", "폰", "커피"]
            ):
                matched_contexts.append(doc["content"])

        if not matched_contexts:
            # 기본 탑재 수면 위생 가이드라인
            return "일정한 조도 유지, 소음 차단, 적정 온도(20-22도) 설정이 수면 건강의 기본 지침입니다."

        return " ".join(matched_contexts)

    def generate_augmented_response(self, question: str, context: str) -> str:
        """
        검색된 도메인 지식(Context)을 프롬프트에 증강(Augment)하여 최종 LLM 답변 스케레톤을 생성합니다.
        """
        # OpenAI 등 LLM API 호출을 모사한 안전한 응답 템플릿
        return f"[RAG AI 분석 결과]\n\n조회된 전문 지식:\n- {context}\n\n코칭 피드백:\n안녕하세요. Sleep Care 365 AI 수면 코치입니다. 질문하신 내용과 연동된 수면 데이터를 기반으로 분석한 결과, 현재 패턴 개선을 위해 위에 제시된 지침을 실천하시는 것을 권장합니다."


# 싱글톤 패턴으로 객체 생성
rag_service = SleepRAGService()
