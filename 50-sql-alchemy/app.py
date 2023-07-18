# https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/#installation
from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    username = StringField('Név', validators=[DataRequired()])
    password = StringField('Jelszó', validators=[DataRequired()])
    email = StringField('E-mail')


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config.from_object('config')
app.secret_key = app.config['WTF_CSRF_SECRET_KEY']

# Adatbázis kapcsolat
db = SQLAlchemy()


class User(db.Model):
    ''' a users tábla létrehozása '''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String)


db.init_app(app)


@event.listens_for(User.__table__, 'after_create')
def add_system_user(*args, **kwargs):
    ''' A users tábla létrehozása után létrehozunk egy felhasználót '''
    print('users tábla létrehozva. Felhasználó beszúrása.')
    u = User(username=app.config['ADMIN_USER']['username'],
             password=app.config['ADMIN_USER']['password'],
             email=app.config['ADMIN_USER']['email'])
    db.session.add(u)
    db.session.commit()


@app.route('/')
@app.route("/users_list")
def users_list():
    users = db.session.execute(
        db.select(User).order_by(User.username)).scalars()
    return render_template('users_list.html', config=app.config, users=users)


@app.route('/user_form', methods=['POST', 'GET'])
@app.route('/user_form/<int:id>')
def user_form(id=None):
    form = UserForm()
    if request.method == "GET":
        if id is not None:
            u = db.session.query(User).get(id)
            form.username = u.username
        return render_template('user_form.html', config=app.config, form=form)
    else:
        u = db.session.query(User).get(id)
        # form_title = request.form["title"]
        # form_year = request.form["year"]
        # movie = Movie(form_title, year=int(form_year) if form_year else None)
        # db = current_app.config["db"]
        # movie_key = db.add_movie(movie)
        return redirect(url_for("movie_page", user=u))

    form = UserForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('user_form.html', form=form)


@app.route('/user_form', methods=['GET', 'POST'])
def submit():
    form = UserForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('user_form.html', form=form)


@app.route('/user_store/', methods=["POST"])
def user_store():
    return render_template('index.html', config=app.config)


@app.route("/user_delete/<int:id>")
def user_delete(id):
    print(f'id={0}'.format(id))
    u = db.session.query(User).get(id)
    # u = db.select(User).where(User.id == 1)
    db.session.delete(u)
    db.session.commit()
    return redirect(url_for('users_list'))


with app.app_context():
    r = db.create_all()


app.run(debug=True, host='0.0.0.0', port=5000)
