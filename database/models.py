from sqlalchemy import Column, String, Integer, Text, DateTime, BigInteger
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.types import NullType

Base = declarative_base()

# UserInfo : 회원정보
class UserInfo(Base):
    __tablename__ = "user_info"

    cphone_no = Column("cphone_no", String(20), primary_key=True, comment="핸드폰번호")
    lgn_pwd = Column("lgn_pwd", String(100), nullable=False, comment="로그인비밀번호")
    ntrydt = Column("ntrydt", DateTime(timezone=True), default=func.now(), comment="가입일")
    moddt = Column("moddt", DateTime(timezone=True), nullable=True, comment="수정일")
    ses_tkn = Column("ses_tkn", String(256), comment="사용중인세션토큰")


# MenuInfo : 메뉴정보
class MenuInfo(Base):
    __tablename__ = "menu_info"

    menu_reg_id = Column("menu_reg_id", String(50), primary_key=True, comment="메뉴등록ID")
    category = Column("category", String(50), primary_key=True, comment="카테고리")
    price = Column("price", BigInteger, nullable=False, comment="가격")
    cost = Column("cost", BigInteger, nullable=False, comment="원가")
    menu_nm = Column("menu_nm", String(100), nullable=False, comment="메뉴명")
    menu_cs_nm = Column("menu_cs_nm", String(100), comment="메뉴초성명")
    destn = Column("destn", Text, comment="설명")
    barcode = Column("barcode", String(100), comment="바코드")
    exprdt = Column("exprdt", DateTime(timezone=True), nullable=False, comment="유통기한")
    size = Column("size", String(10), comment="사이즈")
    regdt = Column("regdt", DateTime(timezone=True), default=func.now(), comment="등록일")
    moddt = Column("moddt", DateTime(timezone=True), nullable=True, comment="수정일")