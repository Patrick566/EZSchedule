from flask import *
from database import init_db, db_session
from models import *

app = Flask(__name__)
app.secret_key = "Key"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        formtype = request.form["form-type"]
        print(formtype)
        if formtype == "signup":
            username = request.form["username"]
            password = request.form["password"]
            if db_session.query(User).where(User.user_name == username).first() is None:
                new_user = User(username, password)
                db_session.add(new_user)
                db_session.commit()
                # flash("You have successfully signed up, Welcome to EZTranslate!", "info")
                session["username"] = username
                return render_template("search.html")
            else:
                flash("Your Username is alread in use, please Login instead", "info")
                return render_template("home.html")
        elif formtype == "login":
            username = request.form["username"]
            password = request.form["password"]
            if db_session.query(User).where((User.user_name == username) & (User.password == password)).first() is not None:
                # flash("You have successfully signed up, Welcome to EZTranslate!", "info")
                session["username"] = username
                return render_template("search.html")
            else:
                flash("You Password or Username is incorrect, please Sign up instead", "info")
                return render_template("home.html")
    if request.method == "GET":
        return render_template("home.html")



@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "GET":
        if "username" in session:
            return render_template("search.html", username=session["username"])
        else:
            return render_template("search.html")
        
    if request.method == "POST":
        search = request.form["search"]
        definition = db_session.query(Word).where(Word.word == search).first()
        if definition is not None:
            return render_template("extension.html", definition = definition)
        else:
            flash("Word does not exist in our database")
        return render_template 
     

@app.route("/dictionary")
def dictionary():
    return render_template("dictionary.html")


if __name__ == "__main__":
    app.run(debug=True)
