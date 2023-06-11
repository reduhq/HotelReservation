from fastapi import FastAPI

app = FastAPI()

@app.get(path="/holamundo")
def holamundo():
    return "Hola mundo"