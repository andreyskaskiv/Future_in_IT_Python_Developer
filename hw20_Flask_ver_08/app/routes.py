from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from app import app, login_manager
from app.UserLogin import UserLogin
from app.database import db, Users, Profiles, ReadDataBase


login_manager.login_view = 'login'
login_manager.login_message = "Авторизуйтесь для доступа к закрытым страницам"
login_manager.login_message_category = "success"


@login_manager.user_loader
def load_user(user_id):
    print("load_user")
    return UserLogin().from_db(user_id, db)


@app.route('/')
@app.route('/index')
def index():
    info = ReadDataBase.get_users(db)
    menu = ReadDataBase.get_navigation(db)

    template = "index.html"
    title = "Главная"
    return render_template(template,
                           title=title,
                           menu=menu, list=info)


@app.route("/about")
@login_required
def about():
    menu = ReadDataBase.get_navigation(db)
    template = "about.html"
    title = "About"
    return render_template(template,
                           title=title,
                           menu=menu)


@app.route("/login", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))

    if request.method == "POST":
        user = ReadDataBase.get_user_by_email(db, request.form['email'])
        if user and check_password_hash(user[0].psw, request.form['psw']):
            userlogin = UserLogin().create(user[0])
            remember_me = True if request.form.get('remainme') else False
            login_user(userlogin, remember=remember_me)
            return redirect(request.args.get("next") or url_for("profile"))

        flash("Неверная пара логин/пароль", "error")

    menu = ReadDataBase.get_navigation(db)
    template = "login.html"
    title = "Login"
    return render_template(template,
                           title=title,
                           menu=menu)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Вы вышли из аккаунта", "success")
    return redirect(url_for('login'))


@app.route('/profile')
@login_required
def profile():
    return f"""<a href="{url_for('logout')}">Выйти из профиля</a>
                user info: {current_user.get_id()}"""



@app.route("/register", methods=("POST", "GET"))
def register():
    if request.method == "POST":

        # add wtforms and CSRF
        if len(request.form['name']) > 4 and len(request.form['email']) > 4 \
                and len(request.form['psw']) > 4 and request.form['psw'] == request.form['psw2']:

            email_request = request.form['email']
            if not ReadDataBase.check_email(db, email_request):

                try:
                    hash_psw = generate_password_hash(request.form['psw'])
                    user = Users(email=request.form['email'], psw=hash_psw)
                    db.session.add(user)
                    db.session.flush()

                    profile = Profiles(name=request.form['name'], old=request.form['old'],
                                       city=request.form['city'], user_id=user.id)

                    db.session.add(profile)
                    db.session.commit()
                except:
                    db.session.rollback()
                    print("Ошибка добавления в БД")

                flash("Вы успешно зарегистрированы", "success")
                return redirect(url_for('login'))

            flash(f"User with this {email_request} already exists")
        else:
            flash("Неверно заполнены поля", "error")

    menu = ReadDataBase.get_navigation(db)
    template = "/register.html"
    title = "Registration"
    return render_template(template,
                           title=title,
                           menu=menu)
