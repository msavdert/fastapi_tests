from fastapi import FastAPI
from routes import router

# FastAPI instance
app = FastAPI()

# Include routes from routes.py
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the GPU Metrics API!"}
