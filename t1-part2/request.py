import requests
import time
import json

def syncMessages(messages, peers):
	while True:
		time.sleep(1/2)
		for url in peers:
			print('Request messages to ' + url + '/messages')
			try:
				r = requests.post(url + '/messages')
				mergeMessages(messages, r.json())
			except requests.exceptions.ConnectionError:
				time.sleep(1/100)


def mergeMessages(messages, new):
	for m in new:
		notIn = True
		for mo in messages:
			if mo[0] == m[0]:
				notIn = False
		if notIn:
			messages.append(m)