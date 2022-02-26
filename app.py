from cs50 import SQL
from database import Database
from flask import Flask, render_template, redirect, flash, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

# Following three blocks from C$50 Finance
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Configure session to use filesystem instead of signed cookies
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = Database(SQL("sqlite:///library.db"))


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/register", methods=["GET, POST"])
def register():
    # Provide form
    if request.method == "GET":
        return render_template("register.html")

    # Make sure email was providedflas
    email = request.form.get("email")
    if not email:
        flash("Email is Required")
        return

    # Make sure email isn't taken
    if email in [user["email"] for user in db.get_users()]:
        flash("Email taken")
        return

    # Make sure password was provided
    password = request.form.get("password")
    if not password:
        flash("Password is required")
        return

    # Make sure passwords match
    if password != request.form.get("confirmation"):
        flash("Passwords don't match")
        return

    # Add info to database
    db.create_user(email, generate_password_hash(password))

    # Provide homepage
    return redirect("/")


@app.route("/login", methods=["GET", "POST"])
def login():
    # Forget any previous user
    session.clear()

    # Provide form
    if request.method == "GET":
        return render_template("login.html")

    # Get email
    email = request.form.get("email")
    if not email:
        flash("Email is required")
        return

    # Get password
    password = request.form.get("password")
    if not password:
        flash("Password is required")

    # Make sure username and password are valid
    user = find_user(email)
    if not user or not check_password_hash(user["hash"], password):
        flash("Invalid username and/or password")
        return

    session["user_id"] = user["id"]
    return redirect("/")


@app.route("/logout")
def logout():
    # Forget any previous user
    session.clear()

    return redirect("/")