'''
chats module:
get chat content
speech to text
'''
import sqlite3
import speech_recognition as sr
from flask import request, jsonify, Blueprint

chats = Blueprint("chats", __name__)
# chats = Flask(__name__)


@chats.route('/chats', methods=['GET'])
def all_chats():
    '''get all chat content'''
    with sqlite3.connect("../database/db.sqlite3") as conn:
        if request.method == 'GET':
            cursor = conn.execute("SELECT * FROM chats")
            chats_list = [
                dict(Chat_ID=row[0], Doctor_ID=row[1],
                     Patient_ID=row[2], Chat_Content=row[3], Date=row[4])
                for row in cursor.fetchall()
            ]
            if chats_list is not None:
                return jsonify(chats_list), 200
    return None


@chats.route('/chat/<int:chat_id>', methods=['GET'])
def single_chat(chat_id):
    '''get single chat'''
    with sqlite3.connect("../database/db.sqlite3") as conn:
        cursor = conn.cursor()
        if request.method == 'GET':
            chat = None
            cursor.execute(
                "SELECT * FROM chats WHERE Chat_ID=?", (chat_id,))
            rows = cursor.fetchall()
            for row in rows:
                if row is not None:
                    chat = row[3]
                    if chat.split('.')[1] == "txt":
                        return print_text(chat), 200
                    return speech_to_text(chat), 200
                return f"Cannot find chat {chat_id}", 404
    return None


def print_text(chat_address):
    '''return text'''
    path = '../chat_record/' + chat_address
    with open(path, encoding="utf-8") as file:
        contents = list(file.readlines())
        return jsonify(contents)


def speech_to_text(chat_address):
    '''convert audio to text'''
    recognizer = sr.Recognizer()
    path = '../chat_record/' + chat_address
    with sr.AudioFile(path) as source:

        audio_text = recognizer.listen(source)

        try:
            # using google speech recognition
            text = ["Converting audio transcripts into text ..."]
            text += [recognizer.recognize_google(audio_text)]
            return jsonify(text)

        except sr.UnknownValueError():
            return 'Sorry.. run again...'


# if __name__ == "__main__":
#     app.run(debug=True)
