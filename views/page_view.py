from flask import Blueprint, render_template

page_provider = Blueprint('page_provider', __name__)


@page_provider.route("/index", endpoint="index")
def index():
    return render_template("index2.html")