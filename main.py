from flask import Flask, render_template

USERNAME = "David Suanov"
app = Flask(__name__)


@app.route("/<string:title>")
@app.route("/index/<string:title>")
def custom_titled_index(title: str) -> str:
    return render_template("index.html", title=title, username=USERNAME)


@app.route("/training/<string:prof>")
def training(prof: str) -> str:
    return render_template("training.html", title="Тренажеры", username=USERNAME, prof=prof.lower())


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
