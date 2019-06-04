import datetime
import os

from flask import Flask

from proxy import Proxy

app = Flask(__name__)


@app.route('/')
def fetch_and_check():
    print('Fetching and checking Proxy')
    connection = os.environ['conn']
    print('starting time', datetime.datetime.now())
    api = Proxy()
    api.get_proxy()
    print('Checking proxy...')
    api.check(CONNECTIONS=int(connection))
    print('ending time', datetime.datetime.now())
    print('Done fetching and checking Proxy')
    return {"code": 200}


@app.route('/fetch')
def fetch():
    print('Fetching Proxy...')
    connection = os.environ['conn']
    print('starting time', datetime.datetime.now())
    api = Proxy()
    api.get_proxy()
    print('ending time', datetime.datetime.now())
    print('Done fetching Proxy')
    return {"code": 200}


@app.route('/check')
def check():
    print('Checking Proxy...')
    connection = os.environ['conn']
    print('starting time', datetime.datetime.now())
    api = Proxy()
    api.get_proxy()
    print('ending time', datetime.datetime.now())
    print('Done checking Proxy')
    return {"code": 200}


if __name__ == '__main__':
    app.run()
