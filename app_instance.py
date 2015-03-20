import connection

#app instance methods
class AppInstance:
  def __init__(self, app, secret):
    self.c = connection.Connection(app, secret)

  def search(self, query, collections = []):
    data = {
      "query": {
        "collections": collections,
        "body": query
      }
    }

    return self.c.req("post", "/~rawsearch", data)
