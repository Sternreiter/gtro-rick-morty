from fastapi import FastAPI
from uvicorn import uvicorn

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)