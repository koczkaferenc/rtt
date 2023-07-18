'''
How to build an application structure?
'''

from flask import Flask, render_template

# Load blueprints
from blueprints.stat_page import stat_page
from blueprints.bp1 import bp1

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config.from_object('config')

# Register all blueprints
app.register_blueprint(stat_page)
app.register_blueprint(bp1)
# maybe it should be the last line


@app.route('/')
def index():
    return render_template('index.html', config=app.config)


app.run(host=app.config["SERVER_ADDRESS"],
        port=app.config["SERVER_PORT"], debug=app.config['DEBUG'])
