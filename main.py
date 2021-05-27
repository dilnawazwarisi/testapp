from flask import Flask
from service import get_message
from redis import Redis

app = Flask(__name__)
# redis = Redis(host='redis-server')


@app.route('/')
def health():
    return 'You are accesing test app API'


@app.route('/<name>')
def hello(name):
    return get_message(name)

@app.route('/hello2')
def hello2():
    return 'Hello2'


@app.route('/hello3')
def hello2():
    return 'Hello3'
# @app.route('/visits/data'):
# def get_visits():


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)