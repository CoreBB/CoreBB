from flask import Flask
from login import login
from register import register
from index import index
from newthread import newthread
import database
from threaddisplay import threaddisplay

app = Flask(__name__)
app.debug = True
app.secret_key = database.getSeed()

app.register_blueprint(index)
app.register_blueprint(login)
app.register_blueprint(register)
app.register_blueprint(newthread)
app.register_blueprint(threaddisplay)

if __name__ == "__main__":
    app.run()
