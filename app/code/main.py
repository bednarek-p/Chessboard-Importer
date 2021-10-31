import aioredis
import uvicorn

from fastapi import (FastAPI, File, UploadFile, Depends, HTTPException,
    Request, status)
from fastapi.responses import JSONResponse
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException

from authorization import User, Auth, Settings
from image_converter import ImageConverter
from read_chessboard import ReadChessboard
from users import users_db

app = FastAPI()


@AuthJWT.load_config
def get_config():
    return Settings()


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )


@app.on_event("startup")
async def startup():
    redis = await aioredis.create_redis_pool("redis://redis")
    FastAPILimiter.init(redis)


@app.post('/login')
def login(user: User, Authorize: AuthJWT = Depends()):
    user = Auth.authenticate_user(users_db, user.username, user.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = Authorize.create_access_token(subject=user.username)
    refresh_token = Authorize.create_refresh_token(subject=user.username)
    return {"access_token": access_token, "refresh_token": refresh_token}


@app.post('/refresh')
def refresh(Authorize: AuthJWT = Depends()):
    Authorize.jwt_refresh_token_required()
    current_user = Authorize.get_jwt_subject()
    new_access_token = Authorize.create_access_token(subject=current_user)
    return {"access_token": new_access_token}


@app.post("/photo", dependencies=[Depends(RateLimiter(times=10, minutes=2))])
async def return_fen(file: UploadFile = File(...),
                    Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    image = ImageConverter.read_image(await file.read())
    fen = ReadChessboard.read_chessboard(image)
    if fen:
        return {"fen":fen}
    raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)


@app.get("/")
def read_root():
    return {"Hello" : "World"}


if __name__== "__main__":
    uvicorn.run(app)
