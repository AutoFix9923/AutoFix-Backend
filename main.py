from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application"}

@app.get("/second")
def second():
    return {"This is second route"}
