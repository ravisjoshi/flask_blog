from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return '<h3>Home Page!</h3>'

@app.route('/books')
def books():
    return '<h3>Books are here!</h3>'

@app.route('/about')
def about():
    return '<h3>Hi, Ravi here!</h3>'

if __name__ == '__main__':
    app.run(debug=True)