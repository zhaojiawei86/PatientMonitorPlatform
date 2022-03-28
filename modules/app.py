'''run programming'''
from flask import Flask
from home import home
from devices import devices
from chats import chats


app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(devices)
app.register_blueprint(chats)

if __name__ == "__main__":
    app.run(debug=True)
