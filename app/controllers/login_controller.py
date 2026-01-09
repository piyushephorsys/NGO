from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.login import LoginRequest
from app.services.loginService import LoginService

loginRouter = APIRouter(prefix="/login", tags=["Login"])
service = LoginService()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@loginRouter.post("/")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    result = service.login(db, request.username, request.password)

    if result["status"] == 403:
        raise HTTPException(status_code=403, detail=result["message"])

    return {
        "status": "success",
        "message": result["message"]
    }
