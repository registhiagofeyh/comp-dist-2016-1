import requests
import time
import json

def connectServer(url, messages, peers):
	messages.append(['Teste', 'Requests'])
	while(1):
		time.sleep(1/2)
		try:
			r = requests.get(url + '/messages/json')
			print(r.text)
			print(json.loads(r.text))
			mergeMessages(messages, r.json())

		except requests.exceptions.ConnectionError:
			time.sleep(1/100)

def mergeMessages(messages, new):
	for m in new:
		if m not in messages:
			messages.append(m)