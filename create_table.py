import sqlite3

# Connect to your database (or create it if it doesn't exist)
conn = sqlite3.connect('portfolio.db')
c = conn.cursor()

# Create the contacts table
c.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        project TEXT,
        message TEXT NOT NULL
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("✅ Table 'contacts' created successfully.")
