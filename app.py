from proxy import Proxy
import datetime



def main():
    print('starting time', datetime.datetime.now())
    api = Proxy()
    api.get_proxy()
    print('ending time', datetime.datetime.now())

if __name__ == '__main__':
    main()