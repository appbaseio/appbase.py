import appbase;
from pubsub import pub

myApp = appbase.app('rest_test', '193dc4d2440146082ea734f36f4f2638');

myC = myApp.collection('user');

print myC.set('sagar', {"name": "sagar"})
print myC.get('sagar');
