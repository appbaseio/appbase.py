import connection
import app_instance

#global methods
def app(app, secret):
  return app_instance.AppInstance(app, secret)
  
def serverTime():
  return connection.req('get', '/time')