import appbase;
from pubsub import pub
from time import sleep

myApp = appbase.app('rest_test', '193dc4d2440146082ea734f36f4f2638');

myC = myApp.collection('user');

#print myC.set('sagar', {"name": "sagar"})
def p(d):
  print "\nrealtime:", d, "\n"

myC.on('sagar', p);
print myC.set('sagar', {"age": 23});
print myC.unset('sagar', "age");
print myC.set('sagar', {"age": 25});
print myC.unset('sagar', ["age", "name"]);
myC.off(p);