from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return redirect("/home")


@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/market")
def market():
    return render_template("market.html")


@app.route("/sdg")
def sdg():
    return render_template("sdg.html")


@app.route("/grid")
def grid():
    # this doesn't exist, so they will be rerouted to home page
    return render_template("grid.html")


if __name__ == '__main__':
    app.run(debug=True)
