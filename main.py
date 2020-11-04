from flask import Flask, render_template
app = Flask(__name__)


@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/project")
def projects():
    return render_template("projects.html")

@app.route("/journal")
def journal():
    return render_template("Ideas.html")

@app.route("/other")
def other():
    return render_template("other.html")

if __name__ == "__main__":
    app.run(debug=True)