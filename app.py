'''run programming'''
from flask import Flask
from modules.home import home
from modules.devices import devices
from modules.chats import chats


app = Flask(__name__)
app.register_blueprint(home)
app.register_blueprint(devices)
app.register_blueprint(chats)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
    # app.run(debug=True)
