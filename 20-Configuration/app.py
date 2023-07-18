'''
Configuration example
Based on http://exploreflask.com/en/latest/configuration.html
The config file and app.py must be placed in the same directory.
'''
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def index():
    return 'Hello, the name of the database is: ' + app.config['DATABASE_NAME'] + ', the first user is: ' + app.config['USERS'][0]


app.run(host=app.config["SERVER_ADDRESS"], port=app.config["SERVER_PORT"])
