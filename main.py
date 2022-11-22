from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    my_name = "Johnny"
    return f'Hello, {my_name}!'