from flask import Flask
from minds import Minds, Profile

app = Flask(__name__)

@app.route('/<input>')
def entry(input):
    pass

#@app.route('/{guid}')

#@app.route('/media/{guid}')

#@app.route('/newsfeed/{guid}')

#@app.route('/blog/view/{guid}')

#@app.route('/user/{guid}')

#@app.route('/group/profile/{guid}')
