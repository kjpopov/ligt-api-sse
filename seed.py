## Sseed data for the hello endpoint
import sqlite3

# Connect to the database
conn = sqlite3.connect('light_api_database.db')
cursor = conn.cursor()

# Define the data to be inserted
data = [
    ('Hello',),
    ('World',),
]

# Create the table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS hello_table (
        id INTEGER PRIMARY KEY,
        word TEXT NOT NULL
    )
''')

# Insert the data into the table
cursor.executemany('INSERT INTO hello_table (word) VALUES (?)', data)

# Commit the changes and close the connection
conn.commit()
conn.close()