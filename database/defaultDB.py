'''
create database for system
'''

import sqlite3
import json
from pathlib import Path
# import time


def create_db(table_path, command):
    '''
    create original device database
    '''

    path = Path(table_path).read_text(encoding="utf8")
    rows = json.loads(path)

    try:
        with sqlite3.connect("db.sqlite3") as conn:
            for row in rows:
                conn.execute(command, tuple(row.values()))
            conn.commit()
    except sqlite3.OperationalError:
        print("No such table. Please create table first.")
    except sqlite3.IntegrityError:
        print("Default table have been existed. Do not create twice.")
    else:
        print("Original table has been created.")


if __name__ == '__main__':
    create_db("../tables/devices.json", "INSERT INTO devices VALUES(?, ?)")
    create_db("../tables/users.json", "INSERT INTO users VALUES(?, ?, ?)")
    create_db("../tables/appointments.json",
              "INSERT INTO appointments VALUES(?, ?, ?, ?, ?, ?, ?)")

    # localtime = time.asctime(time.localtime(time.time()))
    # print("本地时间为 :", localtime)
    # print(type(localtime))
