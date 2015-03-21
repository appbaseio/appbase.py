import config
import errors
import requests
import json

def req(method, url, *data):
  return getattr(requests, method)(config.api_server + url, data=json.dumps(data)).json()

class Connection:
  def __init__(self, app, secret):
    self.base_url = config.api_server + "/" + app + "/" + config.v
    self.headers = {'appbase-secret': secret};

  def req(self, method, url, data):
    if(self.base_url == ""):
      raise Exception(errors.BASE_URL)
    r = getattr(requests, method)(self.base_url + url, data=json.dumps(data), headers=self.headers)
    return r.json()