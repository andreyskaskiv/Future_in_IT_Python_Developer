from flask import render_template, current_app, flash

from app.main import main
from app.auth.models import Users, Profiles


@main.route('/')
def index():
    db = current_app.config['db']
    db.create_tables([Users, Profiles])
    info = Users.select()
    title = "Home"
    return render_template("main/index.html",
                           title=title,
                           list=info)
