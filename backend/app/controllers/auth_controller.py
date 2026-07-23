"""Controller layer for auth. Controllers sit between the router and the
service. They receive validated input, call the service, and return the
result. They hold no business logic themselves.
"""
from sqlalchemy.orm import Session

from app.services.auth_service import AuthService
from app.schemas.user import UserRegister, UserLogin


class AuthController:
    def __init__(self, db: Session):
        self.service = AuthService(db)

    def register(self, data: UserRegister):
        return self.service.register(data)

    def login(self, data: UserLogin):
        return self.service.login(data)
