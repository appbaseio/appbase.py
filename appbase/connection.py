import config
import errors
import requests
import json
from pubsub import pub

def req(method, url, *data):
  return getattr(requests, method)(config.api_server + url, data=json.dumps(data)).json()

class Connection:
  def __init__(self, app, secret):
    self.base_url = config.api_server + "/" + app
    self.headers = {'appbase-secret': secret};
    
    def handleSub(topic):
      if len(pub.getDefaultTopicMgr().getTopic(topic).getListeners()) <= 1:
        self.startStream(topic)

    def handleUnsub(topic):
      if len(pub.getDefaultTopicMgr().getTopic(topic).getListeners()) == 0:
        self.stopStream(topic)
    
    pub.subscribe(handleSub, 'sub')
    pub.subscribe(handleUnsub, 'unsub')

  def req(self, method, url, data={}, params ={}):
    if(self.base_url == ""):
      raise Exception(errors.BASE_URL)
    r = getattr(requests, method)(self.base_url + url, data=json.dumps(data), headers=self.headers)
    try:
      return r.json()
    except ValueError:
      return
    
  def startStream(self, topic): 
    def publish(data):
      pub.sendMessage(topic, data)
      
    
    