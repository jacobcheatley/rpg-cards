from flask import Flask, render_template
from livereload import Server
from sassutils.wsgi import Manifest, SassMiddleware

app = Flask(__name__)
app.wsgi_app = SassMiddleware(
    app.wsgi_app,
    {
        "rpg-cards": Manifest(
            sass_path="static/sass", css_path="static/css", wsgi_path="/static/css", strip_extension=True
        )
    },
)

# An edit


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/style")
def style():
    return render_template("style_test.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
