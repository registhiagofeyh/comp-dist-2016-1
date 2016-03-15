from bottle import run, get, put
import json
import sys


# BUGLIST
# - insercao da mesma chave 2 vezes, possibilita inserir o mesmo par de chave/valer em posicoes diferentes da DHT
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

    def insert(self, k, v):
        for sk in subkeys(k):
            if sk in self.h:
                if not self.h[sk]:
                    self.h[sk] = (k, v)
                    return sk
        return None

    def lookup(self, k):
        for sk in subkeys(k):
            if sk in self.h:
                if self.h[sk]:
                    (ki, vi) = self.h[sk]
                    if ki == k:
                        return vi
        return None

    def __repr__(self):
        return "<<DHT:"+ repr(self.h) +">>"

dht = DHT(sys.argv[2])

@get('/dht/<key>')
def dht_lookup(key):
    global dht
    return json.dumps(dht.lookup(key))

@put('/dht/<key>/<value>')
def dht_insert(key, value):
    global dht
    return json.dumps(dht.insert(key, value))

@get('/debug')
def debug():
    global dht
    return dht.__repr__()

run(host='localhost', port=int(sys.argv[1]))
