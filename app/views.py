#!/usr/bin/env python3
#encoding=utf-8

'''def application(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/html")])
    return ["<h1 style='color:blue'>Hello, World!</h1>".encode("utf-8")]'''

from flask import Flask, request, render_template, redirect, url_for, flash
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from flask_bootstrap import Bootstrap

from app.models import db, User
from app.forms import LoginForm, UserForm, UserForm_Update


app = Flask(__name__)

app.config['SECRET_KEY'] = '\xca\x0c\x86\x04\x98@\x02b\x1b7\x8c\x88]\x1b\xd7"+\xe6px@\xc3#\\'
app.config["SQLALCHEMY_DATABASE_URI"]='mysql+pymysql://root:378540@localhost/platform'
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

#db = SQLAlchemy(app)
db.init_app(app)

login_manager = LoginManager(app)
login_manager.session_protection = "strong"
login_manager.login_view = "login"
#login_manager.init_app(app)

bootstrap = Bootstrap(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=int(user_id)).first() #return User.get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        #print('already login')
        return redirect(url_for('show_index'))
    else:
        if request.method == 'POST':
            user = User.query.filter_by(username=request.form['username']).first()
            #user = User.query.filter_by(username=request.form['username'], pwdhash=request.form['password']).first()
            if user is not None and user.verify_password(request.form['password']):
                login_user(user)
                return redirect(url_for('show_index'))
            else:
                flash('Invalid username or password')
                #return render_template('form.html', message='Bad username or password', username=request.form['username'])

        form = LoginForm()
        return render_template('login.html', form=form)
        #return render_template('form.html')

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for('login'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

'''@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    return render_template("some template")'''

@app.route('/')
@login_required
def show_root():
    return redirect(url_for('show_index'))

@app.route('/index', methods=['GET', 'POST'])
@login_required
def show_index():
    #flash("Welcome to visit our pages.")
    return render_template('index.html', username='admin')

@app.route('/user', methods=['GET', 'POST'])
@login_required
def user_show():
    form = UserForm()
    if request.method == 'GET':
        userlist = User.query.all()
        return render_template('user.html', userlist=userlist, form=form)
    else:
        if form.validate_on_submit():
            user = User(form.username.data, form.password.data, form.role.data)
            db.session.add(user)
            db.session.commit()
            #flash('You have add a new todo list')
        #else:
            #flash(form.errors)
        return redirect(url_for('user_show'))

@app.route('/user_update/<int:id>', methods=['GET', 'POST'])
@login_required
def user_update(id):
    form = UserForm_Update()
    if request.method == 'GET':
        user = User.query.filter_by(id=id).first_or_404()
        #form.id.data = user.id
        form.username.data = user.username
        #form.password.data = user.pwdhash
        form.role.data = user.role
        return render_template('user_update.html', form=form)
    else:
        if form.validate_on_submit():
            user = User.query.filter_by(id=id).first_or_404()
            user.username = form.username.data
            user.role = form.role.data
            db.session.commit()
            #flash('You have update a user')
        #else:
        #    flash(form.errors)
        return redirect(url_for('user_show'))

@app.route('/user_delete/<int:id>')
@login_required
def user_delete(id):
     user = User.query.filter_by(id=id).first_or_404()
     db.session.delete(user)
     db.session.commit()
     #flash('You have delete a user')
     return redirect(url_for('user_show'))

@app.route('/device', methods=['GET', 'POST'])
@login_required
def device_show():
    return render_template('device.html')



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
