import uvicorn
from main import app  # Import the FastAPI app

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)