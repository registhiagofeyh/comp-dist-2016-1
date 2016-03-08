from bottle import run, get, post, view, request, redirect, route, static_file
import sys
import threading
import json

sys.path.append('../t1-part2/')
from request import syncMessages

ID = 0
port = 0
messages = [(ID, "Nobody", "Hello!")]
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
	global ID, port
	m = request.forms.get('message')
	n = request.forms.get('nick')
	ID = ID + 1
	messages.append([str(port) + str(ID), n, m])
	redirect('/' + n)


@route('/static/<path:path>')
def send_static(path):
	return static_file(path, root='static')

for a in sys.argv:
	if a == 'chat.py' or a == sys.argv[1]: continue
	peers.append('http://localhost:' + a)

threading.Thread(target = syncMessages,
	args=[messages, peers]).start()

port = int(sys.argv[1])
run(host='localhost', port=port)

