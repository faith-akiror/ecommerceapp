from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
import os

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
EXPIRE = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)
import os
from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext

pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET = os.getenv("SECRET_KEY")
ALG = os.getenv("ALGORITHM")
EXP = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

def hash_password(p): return pwd.hash(p)
def verify_password(p,h): return pwd.verify(p,h)

def create_token(data):
    data.update({"exp": datetime.utcnow() + timedelta(minutes=EXP)})
    return jwt.encode(data, SECRET, algorithm=ALG)