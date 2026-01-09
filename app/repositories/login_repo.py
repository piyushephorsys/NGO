from sqlalchemy.orm import Session
from app.models.login import Login_User

class UserRepository:

    def find_by_username_and_password(
        self, db: Session, username: str, password: str
    ):
        return db.query(Login_User).filter(
            Login_User.username == username,
            Login_User.password == password
        ).first()
