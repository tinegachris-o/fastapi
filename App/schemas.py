from pydantic import BaseModel # data converion ninto JSON
from fastapi_users import schemas # ready made schemas i.e BaseUser
import uuid

class PostCreate(BaseModel):
    
    title:str
    content:str
    

class PostResponse(BaseModel):
    #id:int
    title:str
    content:str
class UserRead(schemas.BaseUser[uuid.UUID]):
    pass
    
class UserCreate(schemas.BaseUserCreate):
    pass
class UserUpdate(schemas.BaseUserUpdate):
    pass
