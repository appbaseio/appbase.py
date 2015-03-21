import connection
import collection

#app instance methods
class App:
  def __init__(self, app, secret):
    self.c = connection.Connection(app, secret)
    self.name = app

  def search(self, query):
    return self.c.req("post", "/~search", query)
  
  def collection(self, c):
    return collection.Collection(c, self)
  
  
