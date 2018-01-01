from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

# pip3 / pip install flask in terminal (all open a flask project in PyCharm, auto installed to Python packages..)