from bottle import run, get, post, view, request, redirect, route, static_file
import sys
import threading
import json

sys.path.append('../t1-part2/')
from request import *
from peers import *

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


@post('/messages')
def jsonmsgs():
	global messages
	return json.dumps(messages)


@get('/peers/<url>')
def jsonpeers(url):
	global peers
	global port
	if not unpackURL(url) in peers:
		peers.append(unpackURL(url))
	temp = list(peers)
	if port > 0:
		temp.append('http://localhost:' + str(port))
	return json.dumps(temp)


@get('/debug')
def debug():
	global peers
	return json.dumps(peers)


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
threading.Thread(target = syncPeers,
	args=[peers, 'http://localhost:' + str(port)]).start()


run(host='localhost', port=port)

