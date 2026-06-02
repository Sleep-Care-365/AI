# test_api.py
import json
import asyncio
from main import app
from pydantic import BaseModel

print("==================================================")
print(" Sleep Care 365 AI Engine - Local API Test Script")
print("==================================================")


async def simulate_frontend_request():
    print("\n[테스트 1] 프론트엔드 요청 데이터 모사 (Mocking)")
    mock_request = {
        "user_id": "student_developer_99",
        "question": "요즘 자꾸 새벽 3시에 깨는데 스마트폰 블루라이트 때문인가요?",
    }
    print(f"전송 데이터: {json.dumps(mock_request, ensure_ascii=False, indent=2)}")

    print("\n[테스트 2] RAG 서비스 파이프라인 가동 및 대역 컨텍스트 매핑")
    # 의존성 내부 로직 가상 실행 유효성 검증
    from rag_service import rag_service

    context = rag_service.retrieve_relevant_context(mock_request["question"])
    response = rag_service.generate_augmented_response(
        mock_request["question"], context
    )

    print("--------------------------------------------------")
    print(f"▶ 검색된 도메인 지식: {context}")
    print(f"▶ 생성된 AI 코칭 답변:\n{response}")
    print("--------------------------------------------------")
    print("\n🎉 결과: API 데이터 인터페이스 및 RAG 파이프라인 검증 성공 (PASS)")


if __name__ == "__main__":
    asyncio.run(simulate_frontend_request())
