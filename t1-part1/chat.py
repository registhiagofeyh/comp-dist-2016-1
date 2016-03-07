from bottle import run, get, post, view, request, redirect, route, static_file
import sys
import threading
import json

sys.path.append('../t1-part2/')
from request import connectServer

messages = [("Nobody", "Hello!")]
peers = []

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


@get('/messages/json')
def jsonmsgs():
	global messages
	return json.dumps(messages)


@post('/send')
def sendMessage():
    m = request.forms.get('message')
    n = request.forms.get('nick')
    messages.append([n, m])
    redirect('/' + n)


@route('/static/<path:path>')
def send_static(path):
    return static_file(path, root='static')

threading.Thread(target = connectServer,
	args=['http://localhost:' + sys.argv[2], messages, peers]).start()
run(host='localhost', port=int(sys.argv[1]))

