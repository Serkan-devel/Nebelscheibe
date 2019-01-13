from flask import Flask
from minds import Minds, Profile, requires_auth

app = Flask(__name__)
minds_api = Minds()

@app.route('/<input>')
def entry(input):
    pass

#@app.route('/<guid>')
#def fetch_channel(guid):
#    channel_info = 

#@app.route('/<guid>/subscribers')
#def channel_sub(guid):
#    channel-subscbribers = 

#@app.route('/media/<guid>')

@app.route('/newsfeed/<guid>')
def newsfeed(guid):
    content = minds_api.newsfeed_single(guid,None,12)
    return str(content)

@app.route('/newsfeed/top/')
def newsfeed_main():
    timeline_main = minds_api.newsfeed_top(None,12)
    return str(timeline_main)

@app.route('/newsfeed/subscribed/')
def newsfeed_sub():
    timeline_sub = minds_api.newsfeed_subscribed(None,12)
    return str(timeline_sub)

@app.route('/newsfeed/boost/')
def boostfeed():
    boosted_posts = minds_api.newsfeed_boost(None,12)
    return str(boosted_posts)

@app.route('/notifications/<filter>')
@requires_auth
def notifications(filter)
    if filter == 'tags':
        return str(notifications_tags(None,24))
    elif filter == 'comments':
        return str(notifications_comments(None,24))
    elif filter == 'subscriptions':
        return str(notifications_subscriptions(None,24))
    elif filter == 'votes':
        return str(notifications_votes(None,24))
    elif filter == 'reminds':
        return str(notifications_reminds(None,24))
    else:
        return str(notifications_all(None,24))

#@app.route('/blog/view/<guid>')
#def blog_view(guid):
#    

#@app.route('/user/<guid>')

#@app.route('/group/profile/<guid>')
