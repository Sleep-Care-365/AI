# 1. 경량화된 파이썬 3.11 공식 이미지 기반
FROM python:3.11-slim

# 2. 컨테이너 내 작업 디렉토리 설정
WORKDIR /app

# 3. 종속성 설치 효율화를 위해 requirements.txt 먼저 복사
COPY requirements.txt .

# 4. 파이썬 의존성 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 5. RAG AI 엔진 소스 코드 전체 복사
COPY . .

# 6. FastAPI 기본 포트인 8000번 오픈
EXPOSE 8000

# 7. Uvicorn을 활용한 FastAPI 프로덕션 서버 구동 명령 설정
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]