import requests
import time
import json


def syncPeers(peers, selfURL):
	while True:
		time.sleep(1/2)
		for url in peers:
			try:
				r = requests.get(url + '/peers/' + packURL(selfURL))
				mergePeers(peers, r.json(), selfURL)
			except requests.exceptions.ConnectionError as e:
				time.sleep(1)
				continue


def mergePeers(peers, new, selfURL):
	for peer in new:
		if not peer in peers and peer != selfURL:
			peers.append(peer)


def packURL(url):
	new = str(url)
	new = new.replace('://', '___').replace(':', '-').replace('.', '_')
	return new


def unpackURL(url):
	new = str(url)
	new = new.replace('___', '://').replace('-', ':').replace('_', '.')
	return new