'''
Basic Flask Example
To run, open http://127.0.0.1:5000 in your browser.
'''
from flask import Flask

app = Flask(__name__)
app.config_class('config')


@app.route('/')
def index():
    return ('Hello World!')


app.run(host='0.0.0.0', port='5000')
