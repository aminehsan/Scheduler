import traceback
import datetime
import time
import schedule

if __name__ == '__main__':

    @schedule.repeat(schedule.every().friday.at('22:00', tz='Asia/Tehran'), tasks='Tasks-1')
    @schedule.repeat(schedule.every().friday.at('23:00', tz='Asia/Tehran'), tasks='Tasks-2')
    def job(task):
        try:
            now = datetime.datetime.now()
            print(now.strftime('%Y-%m-%d %H:%M:%S'), task)
        except Exception:
            traceback.print_exc()


    while True:
        schedule.run_pending()
        time.sleep(1)
