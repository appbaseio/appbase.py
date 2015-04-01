import connection
import application


#global methods

#appbase.app(app, secret)
def app(appN, secret):
  return application.App(appN, secret)