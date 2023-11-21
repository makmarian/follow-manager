from flask import Flask
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('dev.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        user_name TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS platforms (
        platform_id INTEGER PRIMARY KEY,
        platform_name TEXT NOT NULL,
        platform_url TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS accounts (
        account_id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        platform_id INTEGER NOT NULL,
        username TEXT NOT NULL
    )
''')


#cursor.execute('''
#    INSERT INTO users (user_name, email) VALUES (?, ?)
#''', ('John Doe', 'john.doe@example.com'))

conn.commit()

@app.route('/')
def display_table():

    table_data = [
        {'name': 'John Doe', 'account': "johndoe123", 'platform': 'Pixelfed'}
    ]

    return table_data

if __name__ == '__main__':
    app.run(debug=True, port=5001)
