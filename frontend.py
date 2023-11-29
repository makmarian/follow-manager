from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def display_table():
    return render_template('home.html')

@app.route('/platforms')
def platforms():
    return render_template('platforms.html')

if __name__ == '__main__':
    app.run(debug=True)
