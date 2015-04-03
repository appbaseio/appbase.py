import requests

r = requests.get('https://v3.api.appbase.io/rest_test/user/sagar/~properties?stream=true', headers= {"appbase-secret" : "193dc4d2440146082ea734f36f4f2638"}, stream=True)

for i in r.iter_content():
  print i