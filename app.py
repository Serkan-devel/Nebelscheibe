import responder
from minds-api import minds-api as mds

api = responder.API()

@api.route('/')
def entry():
    pass

@api.route('/media/{m-id}')

@api.route('/newsfeed/{id}')

@api.route('/blog/view/{b-id}')

@app.route('/user/<u-id>')

@app.route('/group/profile/<g-id>')

if __name__ == '__main__':
    api.run()
