import sqlite3
from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import json, uvicorn
from asyncio import sleep
from fastapi.staticfiles import StaticFiles


app = FastAPI()

# Add CORS middleware to the FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def waypoints_generator():
    waypoints = open('waypoints.json')
    waypoints = json.load(waypoints)
    for waypoint in waypoints[0: 30]:
        data = json.dumps(waypoint)
        yield f"event: locationUpdate\ndata: {data}\n\n"
        await sleep(3)

@app.get("/hello")
def hello():
    # Connect to the SQLite database
    conn = sqlite3.connect('light_api_database.db')
    cursor = conn.cursor()

    # Execute a query to fetch a word from the database
    cursor.execute("SELECT word FROM hello_table")
    result = cursor.fetchall()

    # Close the database connection
    cursor.close()
    conn.close()

    if result:
        return {"message": f"Hello, {result}!"}
    else:
        return {"message": "No word found in the database."}

@app.get("/get-waypoints")
async def root():
    return StreamingResponse(waypoints_generator(), media_type="text/event-stream")

app.mount("/", StaticFiles(directory="html", html=True), name="static")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)