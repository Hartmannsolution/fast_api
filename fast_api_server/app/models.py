from sqlalchemy import Column, Integer, String
from database import Base


class UserInfo(Base):
    __tablename__ = "user_indetailfo"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(24), unique=True)
    password = Column(String(70))
    fullname = Column(String(24))


class Blog(Base):
    __tablename__ = "blog"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(24))
    content = Column(String(24))










