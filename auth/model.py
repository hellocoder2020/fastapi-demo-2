from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    username: str = Field(..., example="hellocoder")
    password: str = Field(..., example="hellocoder123")
    fullname: str = Field(..., example="Hello Coder")
    email: str    = Field(..., example="hellocoder@gmail.com")

class UserList(BaseModel):
    id: str
    username: str
    fullname: str
    email: str
    status: str
    created_at: str

class UserPWD(UserList):
    password: str

class Token(BaseModel):
    access_token: str
    token_type  : str
    expired_in  : str
    user_info   : UserList

class TokenData(BaseModel):
    username: str = None