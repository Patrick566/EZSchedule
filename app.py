from flask import *
# from database import init_db, db_session
from models import *

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("home.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    return render_template("search.html")

@app.route("/dictionary")
def dictionary():
    return render_template("dictionary.html")

# @app.before_first_request
# def setup():
#     init_db()

if __name__ == "__main__":
    app.run(debug=True)
