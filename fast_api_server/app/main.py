from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

## regressed back to simple version of main in order to follow tutorial: https://fastapi.tiangolo.com/tutorial/
@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}

@app.get("/test/")
async def read_items():
    return {"msg":"hello world"}