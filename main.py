from fastapi import FastAPI
import restaurant

app = FastAPI()

app.include_router(restaurant.router, prefix="/dishes")
