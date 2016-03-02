from bottle import run, get, post, view, request, redirect, route, static_file


messages = [("Nobody", "Hello!")]


@route('/')
@route('/<name>')
@route('/<name>/')
@view('index')
def index(name='Nobody'):
    return {'nick': name}


@get('/messages')
@view('messages')
def index():
	return {'messages': messages}


@post('/send')
def sendMessage():
    m = request.forms.get('message')
    n = request.forms.get('nick')
    messages.append([n, m])
    redirect('/' + n)


@route('/static/<path:path>')
def send_static(path):
    return static_file(path, root='static')


run(host='localhost', port=8000)
