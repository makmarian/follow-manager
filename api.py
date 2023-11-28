from flask import Flask
import sqlite3
from flask import request
from flask_cors import CORS, cross_origin
from flask import jsonify

app = Flask(__name__)
CORS(app)

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

@app.route('/platforms', methods = ['POST','GET'])
def platforms():
    if request.method == 'POST':
        if not request.data:
            return jsonify({'error': f'no-data-present'}), 400

        name = request.json.get('name')

        if name is None:
            return jsonify({'error': f'no-name-present'}), 400

        conn = sqlite3.connect('dev.db')
        cursor = conn.cursor()

        # Check if platform already exists
        cursor.execute('''SELECT * FROM platforms WHERE platform_name = ?''', (name,))

        if cursor.fetchone():
            return jsonify({'error': f'already-exists'}), 409

        # Add the platform to the database
        cursor.execute('''INSERT INTO platforms (platform_name) VALUES (?)''', (name,))
        conn.commit()

        # Make a check to see that it is actually added
        if cursor.rowcount > 0:
            return jsonify({'success': f'added-platform-{name}'}), 200
        else:
            return jsonify({'error': f'somethign-went-wrong-adding-platform'}), 400

    if request.method == 'GET':
        conn = sqlite3.connect('dev.db')
        cursor = conn.cursor()

        data_list = []
        cursor.execute('''SELECT * FROM platforms''')
        for a in cursor:
            data_list.append(a)

        return jsonify({'data':data_list}), 200

@app.route('/platform/id/<platform_id>', methods=['GET','DELETE'])
def platform_id(platform_id):
    if request.method == 'DELETE':
        conn = sqlite3.connect('dev.db')
        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM platforms WHERE platform_id = ?''', (platform_id,))

        if not cursor.fetchone():
            return jsonify({'error': f'does-not-exist'}), 400
        print(cursor.rowcount)
        cursor.execute('''DELETE FROM platforms WHERE platform_id = ?''', (platform_id,))

        conn.commit()
        print(cursor.rowcount)
        return jsonify({'ff': 'fefe'}), 200



if __name__ == '__main__':
    app.run(debug=True, port=5001)
