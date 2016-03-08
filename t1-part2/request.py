import requests
import time
import json

def syncMessages(messages, peers):
	while(1):
		time.sleep(1/2)
		try:
			for url in peers:
				r = requests.get(url + '/messages/json')
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