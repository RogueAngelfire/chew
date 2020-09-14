import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
def home():
    return render_template("index.html", page_title="Home")


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/")
@app.route("/get_tasks")
def get_tasks():
    tasks = list(mongo.db.chew_tasks.find())
    return render_template("tasks.html", tasks=tasks)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exsists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exsists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # Add new user into a session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check for exsisting user in the Database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # removes user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        ingredients = request.form.get("ingredients").splitlines()
        method = request.form.get("method").splitlines()
        vegetarian = "on" if request.form.get("is_urgent") else "off"
        vegan = "on" if request.form.get("is_urgent") else "off"
        task = {
            "menu_item": request.form.get("menu_item"),
            "menu_name": request.form.get("menu_name"),
            "add_image": request.form.get("add_image"),
            "submitted_by": session["user"],
            "date_submitted": request.form.get("date_submitted"),
            "ingredients": ingredients,
            "method": method,
            "vegetarian": vegetarian,
            "vegan": vegan,
            "protein": request.form.get("protein"),
            "carbs": request.form.get("carbs"),
            "fats": request.form.get("fats"),
            "sugars": request.form.get("sugars"),
            "created_by": request.form.get("created_by"),
            }

        mongo.db.chew_tasks.insert_one(task)
        flash("Recipie Successfully Added")
        return redirect(url_for("get_tasks"))

    categories = mongo.db.menu_categories.find().sort("menu_category_name", 1)
    return render_template("add_task.html", categories=categories)


@app.route("/edit_task/<task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    if request.method == "POST":
        vegetarian = "on" if request.form.get("is_urgent") else "off"
        vegan = "on" if request.form.get("is_urgent") else "off"
        submit = {
            "menu_item": request.form.get("menu_item"),
            "menu_name": request.form.get("menu_name"),
            "add_image": request.form.get("add_image"),
            "submitted_by": request.form.get("submitted_by"),
            "date_submitted": request.form.get("date_submitted"),
            "ingredients": request.form.getlist("ingredients"),
            "method": request.form.getlist("method"),
            "vegetarian": vegetarian,
            "vegan": vegan,
            "protein": request.form.get("protein"),
            "carbs": request.form.get("carbs"),
            "fats": request.form.get("fats"),
            "sugars": request.form.get("sugars"),
            "created_by": session["user"],
        }
        mongo.db.chew_tasks.update({"_id": ObjectId(task_id)}, submit)
        flash("Recipie Successfully Updated")

    task = mongo.db.chew_tasks.find_one({"_id": ObjectId(task_id)})
    categories = mongo.db.menu_categories.find().sort("menu_item", 1)
    return render_template("edit_task.html", task=task, categories=categories)


@app.route("/delete_task/<task_id>")
def delete_task(task_id):
    mongo.db.task.remove({"_id": objectId(taskId)})
    flash("Recipie Removed Successfully")
    return redirect(url_for("get_tasks"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
