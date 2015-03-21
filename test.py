import appbase
myapp = appbase.app('numerous', '2d0b669be5c0d2c63c717d2b8a39d919');
print myapp.search({"query": {"match_all":{}}});
print appbase.serverTime();