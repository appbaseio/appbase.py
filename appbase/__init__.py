import connection
import app


#global methods

#appbase.app(app, secret)
def app(app, secret):
  return app.App(app, secret)

def serverTime():
  return connection.req('get', '/time')