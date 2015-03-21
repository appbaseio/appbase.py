import appbase
myapp = appbase.app('numerous', '2d0b669be5c0d2c63c717d2b8a39d919');
myC = myapp.collection('misc')
print myC.getAll("a646a8c6c4024e6eb4eec2b3bbbc5b0f", {"limit": 3});