from flask import Blueprint, render_template, request, redirect, url_for, abort, flash
from flask_login import login_required, current_user

#? -------------------------- Blueprint --------------------------------
views = Blueprint('views', __name__)

@views.route("/")
def hello_world():
    return "<p>Hello, World!</p>"