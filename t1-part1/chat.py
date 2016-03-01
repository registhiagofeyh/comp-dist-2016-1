from bottle import run, get, post, view, request, redirect, route, static_file


messages = [("Nobody", "Hello!")]
nick = "Nobody"


@get('/')
@view('index')
def index():
    return {'messages': messages, 'nick': nick}


@get('/messages')
@view('messages')
def index():
	return {'messages': messages, 'nick': nick}


@post('/send')
def sendMessage():
    global nick
    m = request.forms.get('message')
    n = request.forms.get('nick')
    messages.append([n, m])
    nick = n
    redirect('/')


@route('/static/<path:path>')
def send_static(path):
    return static_file(path, root='static')


run(host='localhost', port=8000, debug=True)
