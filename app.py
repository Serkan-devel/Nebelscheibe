from flask import Flask
from minds import Minds, Profile

app = Flask(__name__)
minds_api = Minds()

@app.route('/<input>')
def entry(input):
    pass

#@app.route('/{guid}')

#@app.route('/media/{guid}')

@app.route('/newsfeed/<guid>')
def newsfeed(guid):
    content = minds_api.newsfeed_single(guid,None,12)
    return str(content)

#@app.route('/blog/view/{guid}')

#@app.route('/user/{guid}')

#@app.route('/group/profile/{guid}')
