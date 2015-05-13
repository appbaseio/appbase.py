import config
import errors
import requests
import json
import treq
from threading import Thread
from twisted.internet import reactor
from time import sleep

def req(method, url, *data):
  return getattr(requests, method)(config.api_server + url, data=json.dumps(data)).json()

class Connection:
  def __init__(self, app, secret):
    self.base_url = config.api_server + "/" + app
    self.headers = {'appbase-secret': secret};
    self.streams = 0
  
  def req(self, method, url, data={}, params ={}, stream = False):
    if(self.base_url == ""):
      raise Exception(errors.BASE_URL)
    r = getattr(requests, method)(self.base_url + url, data=json.dumps(data), headers=self.headers, stream = stream, params = params)
    try:
      return r.json()
    except ValueError:
      return
  
  def on(self, url, f, params={}):
    if hasattr(f, "_stream"):
      raise Exception(errors.CALLBACK_INUSE + ": " + f._stream)
  
    f._stream = url
    
    #start reactor thread
    if self.streams == 0:
      Thread(target=reactor.run, args=(False,)).start()

    self.streams += 1
    def callback(data):
      if hasattr(f, "_stream") and f._stream == url:
        f(json.loads(data))

    params["streamonly"] = "true"
    reactor.callFromThread(lambda : treq.get(self.base_url + url, headers= self.headers, params = params, stream = True).addCallback(treq.collect, callback))
    sleep(0.3) #wait for it to make the request

  def off(self, f):
    if not hasattr(f, "_stream"):
      raise Exception(errors.CALLBACK_NOT_INUSE)
  
    del f._stream
    self.streams -= 1
    if self.streams == 0:
      reactor.callFromThread(reactor.stop)
    