'''
chats module:
get chat content
speech to text
'''
import os
from concurrent.futures import ThreadPoolExecutor
import sqlite3
# import time
import speech_recognition as sr
from flask import abort, request, jsonify, Blueprint, render_template
from modules import AWS_ADDRESS, PROJ_ADDRESS

S2T = Blueprint("chats", __name__)

# chats = Flask(__name__)
if not os.path.exists(PROJ_ADDRESS):
    PROJ_ADDRESS = AWS_ADDRESS
DB_ADDRESS = PROJ_ADDRESS + "/database/db.sqlite3"
CHAT_ADDRESS = PROJ_ADDRESS + "/chat_record/"


def get_db_connection():
    '''connect db'''
    conn = sqlite3.connect(DB_ADDRESS)
    conn.row_factory = sqlite3.Row
    return conn


def get_post(device_id):
    '''get single device'''
    conn = get_db_connection()
    single_post = conn.execute('SELECT * FROM devices WHERE Device_ID = ?',
                               (device_id,)).fetchone()
    conn.close()
    if single_post is None:
        abort(404)
    return single_post


@S2T.route('/thread-chats/<int:chat_id>')
def run_jobs(chat_id):
    '''multy jobs'''
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.submit(get_single_chat, chat_id)
    return 'Jobs were launched in background!'


@S2T.route('/chat')
def all_chats():
    '''get all chats'''
    if request.method == 'GET':
        conn = get_db_connection()
        allchats = conn.execute('SELECT * FROM chats').fetchall()
        conn.close()
        return render_template('chat_history.html', allchats=allchats)

# @S2T.route('/chats', methods=['GET'])
# def all_chats():
#     '''get all chat content'''
#     with sqlite3.connect(DB_ADDRESS) as conn:
#         if request.method == 'GET':
#             cursor = conn.execute("SELECT * FROM chats")
#             chats_list = [
#                 dict(Chat_ID=row[0], Doctor_ID=row[1],
#                      Patient_ID=row[2], Chat_Content=row[3], Date=row[4])
#                 for row in cursor.fetchall()
#             ]
#             if chats_list is not None:
#                 return jsonify(chats_list), 200
#     return None


# @S2T.route('/chat/<int:chat_id>', methods=['GET'])
# def single_chat(chat_id):
#     '''get single chat'''
#     content = get_single_chat(chat_id)
#     return render_template('chat_single.html', content=content)


@S2T.route('/chat/<int:chat_id>', methods=['GET'])
def single_chat(chat_id):
    '''get single chat'''
    return get_single_chat(chat_id)


def get_single_chat(chat_id):
    '''get single chat'''
    print(f"# Task {chat_id} begin.")
    # time.sleep(5)

    chat_address = get_chat_address(chat_id)

    if chat_address:
        if chat_address.split('.')[1] == "txt":
            text = print_text(chat_address)
            return text, 200
        text = speech_to_text(chat_address)
        print(f"# Task {chat_id} done.")
        return text, 200
    return f"Cannot find chat {chat_id}", 404


def get_chat_address(chat_id):
    '''get chat address'''
    with sqlite3.connect(DB_ADDRESS) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM chats WHERE Chat_ID=?", (chat_id,))
        rows = cursor.fetchall()
        for row in rows:
            if row is not None:
                return row[3]

    return None


def print_text(chat_address):
    '''return text'''
    path = CHAT_ADDRESS + chat_address
    with open(path, encoding="utf-8") as file:
        contents = list(file.readlines())
        print("# Task done.")
        return jsonify(contents)


def speech_to_text(chat_address):
    '''convert audio to text'''
    recognizer = sr.Recognizer()
    path = CHAT_ADDRESS + chat_address
    with sr.AudioFile(path) as source:

        audio_text = recognizer.listen(source)

        try:
            # using google speech recognition
            text = ["Converting audio transcripts into text ..."]
            text += [recognizer.recognize_google(audio_text)]
            print("# Task done.")
            return jsonify(text)

        except sr.UnknownValueError():
            return 'Sorry.. run again...'


# if __name__ == "__main__":
#     app.run(debug=True)
