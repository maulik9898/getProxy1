import datetime
import os

from proxy import Proxy


def main():
    connection = os.environ['conn']
    print('starting time', datetime.datetime.now())
    api = Proxy()
    api.get_proxy()
    print('Checking proxy...')
    api.check(CONNECTIONS=connection)
    print('ending time', datetime.datetime.now())

if __name__ == '__main__':
    main()