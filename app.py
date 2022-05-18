from flask import Flask, render_template, request

app = Flask(__name__)

REGISTRANTS = {}

SPORTS = [
    "Basketball",
    "Soccer",
    "Other"
]


@app.route("/")
def index():
    return render_template("form_index.html", sports=SPORTS)


@app.route("/greet")
def greet():
    name = request.args.get("name", "world")
    return render_template("greet.html", name=name)


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    sport = request.form.get("sport")

    # Validate input
    if not name or not sport or sport not in SPORTS:
        return render_template("failure.html")

    REGISTRANTS[name] = sport

    return render_template("success.html")


@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registants=REGISTRANTS)


if __name__ == '__main__':
    app.run()
