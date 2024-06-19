from datetime import datetime, timedelta
from time import sleep
from schedule import repeat, every, run_pending

if __name__ == '__main__':

    @repeat(every().friday.at('23:00', tz='Asia/Tehran'))
    def job():
        try:
            now = datetime.now()
            print(now)
        except Exception as e:
            print(e)


    while True:
        run_pending()
        sleep(1)
