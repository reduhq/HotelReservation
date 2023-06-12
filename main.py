from fastapi import FastAPI
from db.session import client

app = FastAPI()

@app.get(path="/testing_mongo")
async def testing_mongo():  # Send a ping to confirm a successful connection
    try:
        await client.admin.command('ping')
        return {"response": "Pinged your deployment. You successfully connected to MongoDB!"}
    except Exception as e:
        return {"error": e}