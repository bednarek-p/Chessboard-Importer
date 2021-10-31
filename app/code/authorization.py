import os
from passlib.context import CryptContext
from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str


class Settings(BaseModel):
    authjwt_secret_key: str = os.environ['SECRET']

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Auth:

    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)


    @staticmethod
    def get_password_hash(password):
        return pwd_context.hash(password)


    @staticmethod
    def get_user(data_base, username: str):
        if username in data_base:
            user_dict = data_base[username]
            return User(**user_dict)


    @staticmethod
    def authenticate_user(data_base, username: str, password: str):
        user = Auth.get_user(data_base, username)
        if not user:
            return False
        if not Auth.verify_password(password, user.password):
            return False
        return user
