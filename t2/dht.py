import json
import sys
import requests
from bottle import run, get, put, request
from hashlib import md5
from time import gmtime

# BUGLIST
# - necessario implementar comunicacao em grupo, e propagar os inserts e lookups

def subkeys(k):
    for i in range(len(k), 0, -1):
        yield k[:i]
    yield ""


class DHT:
    def __init__(self, k):
        self.k = k
        self.h = {}

        for sk in subkeys(self.k):
            self.h[sk] = None


    def getNotEmptySK(self, dht):
        r = []
        for sk in dht.h:
            if dht.h[sk] is not None:
                r.insert(r.__len__(), sk)
        return r


    def insert(self, k, v):
        print('Tentando inserir ' + k + ': ' + v)
        for sk in subkeys(k):
            if sk in self.h:
                if not self.h[sk]:
                    if self.lookup(k, True) == None:
                        self.h[sk] = (k, v)
                        print('Inserido em [' + sk + ']')
                        return sk
        return None


    def lookup(self, k, local = False):
        for sk in subkeys(k):
            if sk in self.h:
                if self.h[sk]:
                    (ki, vi) = self.h[sk]
                    if ki == k:
                        return vi
        if not local:
            global peers
            candidates = peers.getNotEmptySK(peers)
            for c in candidates: # somente as chaves da DHT dos peers que foram preenchidas
                # pesquisa se a chave prenchida é parecida com o que está sendo pesquisado
                print(peers.h[c])

        return None


    def __repr__(self):
        return "<<DHT:"+ repr(self.h) +">>"


def mod4md5(string):
    string = md5(string.encode()).hexdigest()
    r = ''
    for c in string:
        r = r + str(ord(c) % 4)

    return r


local_ip = '127.0.0.1'
#init_hash = mod4md5(md5(str(gmtime()).encode()).hexdigest()[:10])
init_hash = mod4md5(local_ip + ':' + str(sys.argv[1]))
print("Inicializando DHT com hash: " + init_hash)
dht = DHT(init_hash)
peers = DHT(init_hash)


@put('/dht/peer/<port>')
def add_peer(port):
    global peers
    remote_ip = request.environ.get('REMOTE_ADDR')
    if (port == None): return None;
    return json.dumps(peers.insert(mod4md5(remote_ip + ':' + str(port)),
        'http://' + remote_ip + ':' + port))


@get('/dht/<key>')
@get('/dht/<key>/')
def dht_lookup(key):
    global dht
    return json.dumps(dht.lookup(mod4md5(key)))


@put('/dht/<key>/<value>')
@put('/dht/<key>/<value>/')
def dht_insert(key, value):
    global dht
    return json.dumps(dht.insert(mod4md5(key), value))


@get('/debug')
@get('/debug/')
def debug():
    global dht, peers
    return dht.__repr__() + "\n\n" + peers.__repr__()

run(host=local_ip, port=int(sys.argv[1]))
