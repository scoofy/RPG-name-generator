from flask import Flask, request, render_template
import dnd_name_gen

app = Flask(__name__)

@app.route("/")
def index():
    return "<table alight='Right'>" + dnd_name_gen.return_html(app) + "</table>"

@app.route("/iama/<dndrace>")
def race(dndrace):
    return "You are a {}".format(dndrace)

@app.route("/meh")
def meh():
    return render_template("meh.html")



























if __name__ == "__main__":
    app.run(debug=True)

