'''run programming'''
from flask import Flask
from modules.home import home
from modules.devices import devices
<<<<<<< HEAD
from modules.speech_to_text import chats
=======
from modules.speech_to_text import S2T
>>>>>>> f8d811e23b722644801d18131a8ae885db95f84e


app = Flask(__name__)
app.register_blueprint(home)
app.register_blueprint(devices)
app.register_blueprint(S2T)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
    # app.run(debug=True)
