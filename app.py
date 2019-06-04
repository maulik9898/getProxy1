import datetime
import os
import time

import requests
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
    api.check(CONNECTIONS=int(connection))
    print('ending time', datetime.datetime.now())
    print('Done checking Proxy')
    return {"code": 200}


def turnOnFetch():
    api = os.environ['API']
    appid = os.environ['APP_ID']
    worker = os.environ['WORKER']
    url = 'https://api.heroku.com/apps/' + appid + '/formation/' + worker
    header = {
        'Accept': 'application/vnd.heroku+json; version=3',
        'Authorization': 'Bearer ' + api
    }
    data = {"quantity": 1, "size": "Free", "type": "worker"}
    response = requests.request("PATCH", url, data=data, headers=header)
    print(response.text)


def turnOffFetch():
    api = os.environ['API']
    appid = os.environ['APP_ID']
    worker = os.environ['WORKER']
    url = 'https://api.heroku.com/apps/' + appid + '/formation/' + worker
    header = {
        'Accept': 'application/vnd.heroku+json; version=3',
        'Authorization': 'Bearer ' + api
    }
    data = {"quantity": 0, "size": "Free", "type": "worker"}
    response = requests.request("PATCH", url, data=data, headers=header)
    print(response.text)


if __name__ == '__main__':

    schedule.every(2).minutes.do(check)
    schedule.every().day.at('00:00').do(turnOnFetch)
    schedule.every().day.at('00:30').do(turnOffFetch)
    schedule.every().day.at('2:00').do(turnOnFetch)
    schedule.every().day.at('2:30').do(turnOffFetch)
    schedule.every().day.at('4:00').do(turnOnFetch)
    schedule.every().day.at('4:30').do(turnOffFetch)
    schedule.every().day.at('5:00').do(turnOnFetch)
    schedule.every().day.at('5:30').do(turnOffFetch)
    schedule.every().day.at('6:00').do(turnOnFetch)
    schedule.every().day.at('6:30').do(turnOffFetch)
    schedule.every().day.at('7:00').do(turnOnFetch)
    schedule.every().day.at('7:30').do(turnOffFetch)
    schedule.every().day.at('8:00').do(turnOnFetch)
    schedule.every().day.at('8:30').do(turnOffFetch)
    schedule.every().day.at('9:00').do(turnOnFetch)
    schedule.every().day.at('9:30').do(turnOffFetch)
    schedule.every().day.at('10:00').do(turnOnFetch)
    schedule.every().day.at('10:30').do(turnOffFetch)
    schedule.every().day.at('11:00').do(turnOnFetch)
    schedule.every().day.at('11:30').do(turnOffFetch)

    while True:
        # Checks whether a scheduled task
        # is pending to run or not
        schedule.run_pending()
        time.sleep(10)
    