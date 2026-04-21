import uuid
from datetime import datetime # Added this import
from collections.abc import AsyncGenerator
from sqlalchemy import Column, String, Text, DateTime,ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase,relationship
from fastapi_users.db  import SQLAlchemyBaseUserTableUUID,SQLAlchemyUserDatabase
from fastapi import Depends
DATABASE_URL = "sqlite+aiosqlite:///./test.db"#file db not normal db

class Base(DeclarativeBase):#Tables are Created
    pass
class User(SQLAlchemyBaseUserTableUUID,Base):
    posts=relationship("Post",back_populates="user")
class Post(Base):#Defines my tables
    __tablename__ = "posts"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    caption = Column(Text)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=False)
    #user_id=Column(UUID(as_uuid=True),ForeignKey=("user.id"),nullable=False)
    url = Column(String, nullable=False)
    file_type = Column(String, nullable=False)
    file_name = Column(String, nullable=False)
    # Corrected the default here
    created_at = Column(DateTime, default=datetime.utcnow)
    user=relationship("User",back_populates="posts")

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)#Make new work sessions


async def create_db_and_tables():
    async with engine.begin() as conn:#Creates test.db  file
        await conn.run_sync(Base.metadata.create_all)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

async def get_user_db(session:AsyncSession= Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)