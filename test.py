import appbase;
from pubsub import pub

def p(data):
  print "\n\nrealtime: ", d, "\n\n"

myApp = appbase.app('rest_test', '193dc4d2440146082ea734f36f4f2638');
print myApp.search({"query": { "match_all" : {}}});
print myApp.listCollections();
print myApp.serverTime();

myC = myApp.collection('user');

print myC.insert({"foo": "bar"});
print myC.set('sagar', {"name": "sagar"})
myC.on('sagar', p);
print myC.set('sid', {"name": "sid"})
print myC.get('sagar');
print myC.getAll({"limit": 3});
print myC.set('sagar', {"age": 23});
print myC.unset('sagar', "age");
print myC.unset('sagar', ["age", "name"]);
print myC.search({"query": { "match_all" : {}}});
print myC.setRef('sagar', 'friend', 'user/sid');
print myC.getRefs('sagar');
print myC.unsetRef('sagar', ['friend']);
print myC.getRefs('sagar');
print myC.delete('sagar');
myC.off(p);