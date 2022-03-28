from flask import Flask
from example_blueprint import example_blueprint
from devices import devices
from chats import chats


app = Flask(__name__)

app.register_blueprint(example_blueprint)
app.register_blueprint(devices)
app.register_blueprint(chats)

if __name__ == "__main__":
    app.run(debug=True)
