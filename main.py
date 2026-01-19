#main entry point for this project
from app.logics import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        app = "app.logics:app", #(1st app is the folder name, 2nd app is the file name, 3rd app is the FastAPI object name)
        host = "127.0.0.1",
        port = 8081,
        reload=True
    )