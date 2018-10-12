from flask import Flask
from minds-api import minds-api as mds

app = Flask(__name__)

@app.route('/')
def entry():
    pass

@app.route('/media/<m-id>')

@app.route('/newsfeed/<id>')

@app.route('/blog/view/<b-id>')

@app.route('/user/<u-id>')

@app.route('/group/profile/<g-id>')
