import connection

#app instance methods
class App:
  def __init__(self, app, secret):
    self.c = connection.Connection(app, secret)

  def search(self, query):
    return self.c.req("post", "/~search", query)
