import treq
from threading import Thread
from twisted.internet import reactor
from time import sleep
import json
Thread(target=reactor.run, args=(False,)).start()

def f(d):
  print json.loads(d)

reactor.callFromThread(lambda : treq.get('https://v3.api.appbase.io/rest_test/user/sagar/~properties', headers= {"appbase-secret" : "193dc4d2440146082ea734f36f4f2638"}, params={"stream" : "true"}, stream=True).addCallback(treq.collect, f))

print "done"

sleep(15)
reactor.callFromThread(reactor.stop)
