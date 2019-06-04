import datetime
import os
import time

import schedule

from proxy import Proxy


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


def fetch():
    print('Fetching Proxy...')
    connection = os.environ['conn']
    print('starting time', datetime.datetime.now())
    api = Proxy()
    api.get_proxy()
    print('ending time', datetime.datetime.now())
    print('Done fetching Proxy')
    return {"code": 200}


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

    schedule.every(2).minutes.do(check)
    while True:
        # Checks whether a scheduled task
        # is pending to run or not
        schedule.run_pending()
        time.sleep(10)
    fetch_and_check()
