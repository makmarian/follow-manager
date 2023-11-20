from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def display_table():
    # Sample data for the table
    table_data = [
        {'name': 'John Doe', 'account': "johndoe123", 'platform': 'Pixelfed'}
    ]

    return render_template('table.html', table_data=table_data)

if __name__ == '__main__':
    app.run(debug=True)
