from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config.from_object('config')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/adatvedelem')
def adatvedelem():
    return render_template('adatvedelem.html', config=app.config)


if __name__ == '__main__':
    app.run(debug=True)
