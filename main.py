from fastapi import FastAPI
from random import randint

app = FastAPI()

@app.get("/randomId")
async def get_number(id: int):
    result = str(id * 2022 + randint(1, 10))
    return {"response": result}
