from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles
from starlette.responses import HTMLResponse
from minds import Minds, Profile
import uvicorn

app = Starlette(debug=True, template_directory='templates')
app.mount('/static', StaticFiles(directory='static'), name='static')

@app.route('/{input}')
def entry(input):
    template = app.get_template('base.html')
    content = template.render(page_title=input)
    return HTMLResponse(content)

#@app.route('/{guid}')

#@app.route('/media/{guid}')

#@app.route('/newsfeed/{guid}')

#@app.route('/blog/view/{guid}')

#@app.route('/user/{guid}')

#@app.route('/group/profile/{guid}')

if __name__ == '__main__':
    uvicorn.run(app)
