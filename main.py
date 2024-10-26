import traceback
import datetime
import time
import json
import pathlib
import schedule


def read_json(path: str) -> dict | list:
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        print(f"A json file was read with the name of '{pathlib.Path(path).name}'.")
        return data


if __name__ == '__main__':

    @schedule.repeat(schedule.every().friday.at('22:00', tz='Asia/Tehran'), tasks='Tasks-1')
    @schedule.repeat(schedule.every().friday.at('23:00', tz='Asia/Tehran'), tasks='Tasks-2')
    def job_1(task):
        try:
            now = datetime.datetime.now()
            print(now.strftime('%Y-%m-%d %H:%M:%S'), task)
        except Exception:
            traceback.print_exc()

# OR

    input_tasks = read_json(path='tasks.json')
    @schedule.repeat(schedule.every().friday.at('23:00', tz='Asia/Tehran'), tasks=('', input_tasks))
    def job_2(tasks: tuple[str, list]):
        try:
            now = datetime.datetime.now()
            for task in tasks[1]:
                timestamp = {
                    'now': int(now.timestamp()),
                    'previous': int((now - datetime.timedelta(days=7)).timestamp())
                }
                task.update({'metaData': {'timestamp': timestamp}})
            print(now.strftime('%Y-%m-%d %H:%M:%S'), tasks[0])
        except Exception:
            traceback.print_exc()


    while True:
        schedule.run_pending()
        time.sleep(1)
