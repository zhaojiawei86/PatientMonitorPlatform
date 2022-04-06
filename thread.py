import os
import time
from flask import Flask, jsonify
from threading import Thread

app = Flask(__name__)
app.secret_key = os.urandom(42)


def threaded_task(duration):

    print("Begin working with thread {}".format(duration))
    time.sleep(5)
    print("Thread {} done".format(duration))


# @app.route("/", defaults={'duration': 5})
@app.route("/<int:duration>")
def index(duration):
    thread = Thread(target=threaded_task, args=(duration,))
    thread.daemon = True
    thread.start()
    return jsonify({'thread_name': str(thread.name),
                    'started': True})


if __name__ == '__main__':
    app.run()
