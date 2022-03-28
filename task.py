from flask import Flask
from time import sleep
from concurrent.futures import ThreadPoolExecutor

# DOCS https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor
# executor = ThreadPoolExecutor(10)

app = Flask(__name__)


@app.route('/jobs')
def run_jobs():
    with ThreadPoolExecutor(max_workers=10) as executor:
        future = executor.submit(some_long_task1)
        print(future.result())

        future2 = executor.submit(some_long_task2, 'hello', 123)

        print(future2.result())

    # executor.submit(some_long_task1)
    # executor.submit(some_long_task2, 'hello', 123)
    return 'Two jobs were launched in background!'


def some_long_task1():
    print("Task #1 started!")
    sleep(2)
    print("Task #1 is done!")
    return "task1"


def some_long_task2(arg1, arg2):
    print("Task #2 started with args: %s %s!" % (arg1, arg2))
    sleep(2)
    print("Task #2 is done!")
    return "task2"


if __name__ == '__main__':
    app.run()
