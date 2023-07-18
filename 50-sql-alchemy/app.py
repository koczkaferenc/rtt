# https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/#installation
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config.from_object('config')

# Adatbázis kapcsolat
db = SQLAlchemy()
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html', config=app.config)

@app.route("/users_list")
def users_list():
    users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    return render_template('users_list.html', config=app.config, users=users)

@app.route('/userform/<int:id>')
def userform(id):
    pass

@app.route('/user_store/', methods=["POST"])
def user_store():
    u = User(username='Koczka Ferenc',email='info@linux-szerver.hu')
    db.session.add(u)
    db.session.commit()
    return render_template('index.html', config=app.config)

@app.route("/user_delete/<int:id>")
def user_delete(id):
    pass


with app.app_context():
    db.create_all()

app.run(debug=True, host='0.0.0.0', port=5000)