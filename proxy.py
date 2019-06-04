import concurrent
import os
import time
from concurrent.futures.thread import ThreadPoolExecutor

import pyrebase
import requests
import urllib3


class Proxy(object):
    ENDPOINT = 'http://torrentapi.org/pubapi_v2.php'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    }
    firebaseConfig = {
        'apiKey': os.environ['apiKey'],
        'authDomain': os.environ['authDomain'],
        'databaseURL': os.environ['databaseURL'],
        'projectId': os.environ['projectId'],
        'storageBucket': os.environ['storageBucket'],
        'messagingSenderId': os.environ['messagingSenderId'],
        'appId': os.environ['appId']
    }

    def __init__(self) -> None:
        super().__init__()
        self.header = self.HEADERS
        self.firebase = pyrebase.initialize_app(self.firebaseConfig)
        self.db = self.firebase.database()

    def get_proxy_thread(self, p):
        pl = []
        url = p
        resp = requests.get(url)
        if 'error' not in resp.json():
            pl.append(resp.json())
            proxy = resp.json()['ip'] + ':' + str(resp.json()['port'])
            type = resp.json()['protocol']
            proxys = {
                type: type + '://' + proxy
            }
            self.db.child('ip').child().push(resp.json())
            return proxy
        else:
            return 'error'

    def db_push(self, data):
        self.db.child('ip').child().push(data)

    def get_db(self):
        return self.db

    def is_bad_proxy(self,pip, key):
        try:
            proxy_handler = urllib3.ProxyManager('http://' + pip)
            HEADERS = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
            }
            req = proxy_handler.request('GET',
                                        'http://torrentapi.org/pubapi_v2.php&get_token=get_token?app_id=proxycheck',
                                        headers=HEADERS, timeout=2)  # change the url address here
        except urllib3.exceptions.HTTPError as e:
            print('Error code: ', e)
            self.db.child('ip').child(key).remove()
            return e
        except Exception as detail:
            print("ERROR:", detail)
            return 1
        return 0

    def get_proxy(self):
        out = ['https://api.getproxylist.com/proxy?lastTested=600&protocol=http&allowsHttps=1&country=US&maxConnectTime=.5&maxSecondsToFirstByte=.5'] * 25
        with ThreadPoolExecutor(max_workers=25) as executor:
            future_to_url = (executor.submit(self.get_proxy_thread, p) for p in out)
            time1 = time.time()
            for future in concurrent.futures.as_completed(future_to_url):
                try:
                    data = future.result()
                    if data is not 'error':
                        print(data)
                    else:
                        print('error')
                    # do json processing here
                except Exception as exc:
                    print('generated an exception',  exc)

            time2 = time.time()
        print(f'Total time took for fetching proxies {time2 - time1:.2f} s')

    def check(self, CONNECTIONS=10):
        out = []
        plist = self.db.child('ip').get()
        print('Total Proxies : ',len(plist.val()))
        with concurrent.futures.ThreadPoolExecutor(max_workers=CONNECTIONS) as executor:
            future_to_url = (executor.submit(self.is_bad_proxy, p.val()['ip'] + ':' + str(p.val()['port']), p.key()) for
                             p in plist.each() if 'ip' in p.val())
            time1 = time.time()
            for future in concurrent.futures.as_completed(future_to_url):
                try:
                    data = future.result()
                except Exception as exc:
                    data = str(type(exc))

            time2 = time.time()

        plist = self.db.child('ip').get()
        print('Total active Proxies : ', len(plist.val()))
        print(f'Time took to check proxies {time2 - time1:.2f} s')

    def getdb(self):
        return self.db
