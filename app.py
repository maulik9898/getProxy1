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
    print('Turning on App')
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
    print('Turning off App')
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
    
    fetch_and_check()

    schedule.every(30).minutes.do(check)

    schedule.every().day.at('06:00').do(turnOnFetch)
    schedule.every().day.at('06:58').do(turnOffFetch)
    schedule.every().day.at('07:00').do(turnOnFetch)
    schedule.every().day.at('07:58').do(turnOffFetch)
    schedule.every().day.at('08:00').do(turnOnFetch)
    schedule.every().day.at('08:58').do(turnOffFetch)
    schedule.every().day.at('09:00').do(turnOnFetch)
    schedule.every().day.at('09:58').do(turnOffFetch)


    while True:
        # Checks whether a scheduled task
        # is pending to run or not
        schedule.run_pending()
        time.sleep(10)
    