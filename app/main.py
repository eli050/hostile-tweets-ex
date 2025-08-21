from manager import Manager
from fastapi import FastAPI
from contextlib import asynccontextmanager


data = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global data
    try:
        data = Manager.pypeline()
        yield
    finally:
        data = None

app = FastAPI(lifespan=lifespan)

@app.get("/data")
def get_data():
    """Endpoint to fetch processed data."""
    if data is None:
        return {"error": "Data not available"}
    return data

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)


