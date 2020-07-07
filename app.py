from config import app
from views.data_view import data_provider
from views.page_view import page_provider
from flask import redirect, url_for

app.register_blueprint(data_provider, url_prefix="/data")
app.register_blueprint(page_provider, url_prefix="/page")


@app.route("/")
def home():
    return redirect("/page/index", 302)


if __name__ == "__main__":
    app.run()
