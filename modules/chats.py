import time
import sqlite3


def get_chat():
    with sqlite3.connect("../database/db.sqlite3") as conn:
        command = "SELECT * FROM chats"
        cursor = conn.execute(command)
        return cursor.fetchall()


def save_chat(Doctor_ID, Patient_ID, Chat_Content):
    Date = time.asctime(time.localtime(time.time()))
    with sqlite3.connect("../database/db.sqlite3") as conn:
        command = "INSERT INTO chats(Doctor_ID, Patient_ID, Chat_Content, Date) VALUES (?, ?, ?, ?)"
        conn.execute(command, (Doctor_ID, Patient_ID, Chat_Content, Date,))
        conn.commit()


if __name__ == "__main__":
    # save_chat(2, 3, "Hello2")

    Date = time.asctime(time.localtime(time.time()))
    with sqlite3.connect("../database/db.sqlite3") as conn:
        command1 = "UPDATE sqlite_sequence SET seq = 0 WHERE name = chats"
        command2 = "INSERT INTO chats(Doctor_ID, Patient_ID, Chat_Content, Date) VALUES (?, ?, ?, ?)"
        conn.execute(command2, (0, 0, "Chat_Content", Date,))
        conn.commit()

    chat = get_chat()
    print(chat)
