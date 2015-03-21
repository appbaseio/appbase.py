import uuid

class Collection:
  def __init__(self, collection, appInst):
    self.app = appInst
    self.name = collection
    self.path = "/" + collection
    
  def docPath(self, doc_subpath):
    return self.path + "/" + doc_subpath
    
  def search(self, query):
    return self.app.c.req("post", self.path + "/~search", query)
  
  def insert(self, data):
    key = str(uuid.uuid4()).replace("-", "")
    return self.app.c.req("patch", self.docPath(key) + "/~properties", data)
  
  def set(self, key, data):
    return self.app.c.req("patch", self.docPath(key) + "/~properties", data)
  
  def get(self, key):
    return self.app.c.req("get", self.docPath(key) + "/~properties")
  
  def delete(self, key):
    return self.app.c.req("delete", self.docPath(key) + "/~properties")
  
  def getAll(self, key, filters = {}):
    return self.app.c.req("get", self.path + "/~list", params = filters)