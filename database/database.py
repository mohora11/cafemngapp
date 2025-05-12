from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DB 연결 URL 설정 (예시로 MySQL을 사용한다고 가정)
DATABASE_URL = "mysql+mysqlconnector://username:z1s2c3f4##@localhost/cafe_db"

# SQLAlchemy 엔진 생성
engine = create_engine(DATABASE_URL, pool_recycle=3600)

# 세션 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base 클래스 설정
Base = declarative_base()

# 데이터베이스 세션을 얻는 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()