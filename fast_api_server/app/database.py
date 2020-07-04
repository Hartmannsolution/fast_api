from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# for password with special chars we need url encoding: import urllib.parse; urllib.parse.quote_plus("somestrangepasswordkx%jj5/g"); # will return the encoded password to put in the connectionsstring

# dialect+driver://username:password@host:port/database
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:root@db:3306/restapi"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
