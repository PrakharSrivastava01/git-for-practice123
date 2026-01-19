from fastapi import FastAPI
from routers import metrics, social

app = FastAPI(
    title = "DevOps Api",
    description = "This is a demo API for DevOps Project",
    version = "1.0.0",
    doc_url = "/docs",
    redoc_url="/redocs"
)
@app.get("/home")
def greet():
    """
    This is sample API for greeting:- If this screen is visible, it means your FastAPI is working fine.
    My 1st API. Thanks to Shubham bhaiya for teaching FastAPI.
    """
    return{"message" : "Hello World..! FastAPI is working fine..!"}

app.include_router(metrics.router)
app.include_router(social.router)
