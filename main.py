from fastapi import FastAPI
from api.cafe import router as cafe_router

# FastAPI 애플리케이션 생성
app = FastAPI()

# 라우터 등록
app.include_router(cafe_router)