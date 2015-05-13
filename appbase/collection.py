import uuid

class Collection:
  def __init__(self, collection, appInst):
    self.app = appInst
    self.name = collection
    self.path = "/" + collection
    self.listeners = {};
    
  def docPath(self, doc_subpath):
    return self.path + "/" + doc_subpath
    
  def search(self, query):
    return self.app.c.req("post", self.path + "/~search", query)
  
  def insert(self, data):
    key = str(uuid.uuid4()).replace("-", "")
    return self.app.c.req("patch", self.docPath(key) + "/~properties", data)
  
  def set(self, key, data):
    return self.app.c.req("patch", self.docPath(key) + "/~properties", data)
  
  def unset(self, key, props):
    if isinstance(props, list):
      return self.app.c.req("delete", self.docPath(key) + "/~properties", { "properties": props})
    else:
      return self.app.c.req("delete", self.docPath(key) + "/~properties", { "properties": [props]})
  
  def get(self, key):
    return self.app.c.req("get", self.docPath(key) + "/~properties")
  
  def on(self, key, f):
    return self.app.c.on(self.docPath(key) + "/~properties", f)
  
  def off(self, f):
    return self.app.c.off(f)
  
  def onDocuments(self, f):
    return self.app.c.on(self.path + "/~documents", f)
  
  def onRef(self, key, f):
      return self.app.c.on(self.docPath(key) + "/~references", f)
  
  def setRef(self, key, ref, path, priority = None):
    return self.app.c.req("patch", self.docPath(key) + "/~references", {ref: { "path": path, "priority": priority}})
  
  def unsetRef(self, key, props):
    if isinstance(props, list):
      return self.app.c.req("delete", self.docPath(key) + "/~references", {"references": props})
    else:
      return self.app.c.req("delete", self.docPath(key) + "/~references", {"references": [props]})
  
  def getRefs(self, key, filters = {}):
    return self.app.c.req("get", self.docPath(key) + "/~references", params = filters)
  
  def delete(self, key):
    return self.app.c.req("delete", self.docPath(key), { "all" : True})
  
  def getAll(self, key, filters = {}):
    return self.app.c.req("get", self.path + "/~documents", params = filters)