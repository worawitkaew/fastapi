from fastapi import FastAPI

app = FastAPI()
                 
@app.get("/")
def root():
    return {"message": "Hello Worl"}

@app.get("/a")
def roota():
    return {"message": "Hello Worl"}
