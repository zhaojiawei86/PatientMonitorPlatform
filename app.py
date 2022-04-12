'''run programming'''
import secrets
from flask import Flask
from modules.home import home
from modules.devices import devices
from modules.speech_to_text import S2T
from modules.appointments import apts


app = Flask(__name__)
app.register_blueprint(home)
app.register_blueprint(devices)
app.register_blueprint(S2T)
app.register_blueprint(apts)


secret_key = secrets.token_hex(16)
app.config['SECRET_KEY'] = secret_key


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
    # app.run(debug=True)
