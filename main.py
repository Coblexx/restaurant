from fastapi import FastAPI
import restaurant

app = FastAPI()

app.include_router(restaurant.router, prefix="/students")


@app.get("/")
async def root():
    return {"message": "Hello World"}