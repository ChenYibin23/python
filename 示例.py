from flask import Flask

app = Flask(__name__)


@app.route('/')
def aaa():
    return('aaa aaa')


if __name__ == '__main__':
    app.run()
