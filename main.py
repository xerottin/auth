from fastapi import FastAPI, Depends
from sqlalchemy import MetaData


app = FastAPI()


@app.post("/register/")
async def register_user():
    return {"message": "User registered and email sent!"}
