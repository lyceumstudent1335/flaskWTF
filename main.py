from flask import Flask, render_template

app = Flask(__name__)


@app.route("/<string:title>")
@app.route("/index/<string:title>")
def custom_titled_index(title: str):
    return render_template("index.html", title=title, username="David Suanov")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
