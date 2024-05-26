from fastapi import FastAPI
import sqlite3

app = FastAPI()

@app.get("/hello")
def hello():
    # Connect to the SQLite database
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    # Execute a query to fetch a word from the database
    cursor.execute("SELECT word FROM your_table LIMIT 1")
    result = cursor.fetchone()

    # Close the database connection
    cursor.close()
    conn.close()

    if result:
        return {"message": f"Hello, {result[0]}!"}
    else:
        return {"message": "No word found in the database."}