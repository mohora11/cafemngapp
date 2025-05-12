from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import models, database

router = APIRouter(prefix="/cafe")

# DB 세션을 받아오는 의존성 함수
def get_db_session(db: Session = Depends(database.get_db)):
    return db

# 회원가입 처리 API (기존의 회원가입 로직을 활용)
@router.post("/userntry")
async def user_entry(username: str, password: str, db: Session = Depends(get_db_session)):
    db_user = db.query(models.UserInfo).filter(models.UserInfo.cphone_no == username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="이미 등록된 사용자입니다.")
    
    # 새 사용자 생성
    new_user = models.UserInfo(cphone_no=username, lgn_pwd=password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"message": "회원가입 성공", "cphone_no": new_user.cphone_no}

# 메뉴 목록 조회 API
@router.get("/menulist")
async def get_menu_list(db: Session = Depends(get_db_session)):
    menus = db.query(models.MenuInfo).all()
    return {"menus": menus}

# 특정 메뉴 조회 API
@router.get("/menu/{menu_reg_id}")
async def get_menu_detail(menu_reg_id: str, db: Session = Depends(get_db_session)):
    menu = db.query(models.MenuInfo).filter(models.MenuInfo.menu_reg_id == menu_reg_id).first()
    if not menu:
        raise HTTPException(status_code=404, detail="메뉴를 찾을 수 없습니다.")
    
    return {"menu": menu}