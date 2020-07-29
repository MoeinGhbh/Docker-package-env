from flask import Flask
from pkg.mypkg import Moein

app = Flask(__name__)

@app.route("/")
def hello():
    moein = Moein()
    return moein.moein_print()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
