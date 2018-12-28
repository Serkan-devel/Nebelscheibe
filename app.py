import responder
from minds import Minds, Profile

api = responder.API()

@api.route('/')
def entry():
    pass

@api.route('/{guid}')

@api.route('/media/{guid}')

@api.route('/newsfeed/{guid}')

@api.route('/blog/view/{guid}')

@app.route('/user/{guid}')

@app.route('/group/profile/{guid}')

if __name__ == '__main__':
    api.run()
