# Python Wrapper for Appbase


Importing
```
import appbase
```

## 1) Global

```python
#generate a uuid (client side)
id = appbase.uuid()
```

## 1) App Instance

```python
myApp = appbase.app('app', 'secret')

#server time - in milliseconds - http://docs.appbase.io/#/v3.0/rest/api-reference#api-reference-global-server-time
time = myApp.serverTime()

#search - http://docs.appbase.io/#/v3.0/rest/api-reference#api-reference-global-search-collections
myApp.search(query = {})
```

## 2) Collection
```python
#collections - http://docs.appbase.io/#/v3.0/rest/api-reference#api-reference-global-list-collections
arrayOfCollections = myApp.listCollections();

#access
myCollection = myApp.collection("user");
myCollection.search(query = {}); 
#http://docs.appbase.io/#/v3.0/rest/api-reference#api-reference-collection-search-documents-by-propertyies

#listen - creation/removal of documents in the whole collections
myCollection.onDocuments(callbackFunction)

 #stop any callback from listening
 myCollection.off(theSamecallbackFunction)
```

## 3) Documents
```python
#1 insert - uses http://docs.appbase.io/#/v3.0/rest/api-reference#api-reference-document-properties-create-update-document-properties
inserted_doc = myCollection.insert(data)

#2 get one document - http://docs.appbase.io/#/v3.0/rest/api-reference#api-reference-document-properties-read-document-properties
data = myCollection.get('id') # returns a dictionary
# id could be a path as well ("sagar/tweets/tweet1")

#3 get all documents document - http://docs.appbase.io/#/v3.0/rest/api-reference#api-reference-collection-list-all-documents
arrayOfdocuments = myCollection.getAll() # returns an array
	#3.1 limit and skip (filters)
	arrayOfdocuments = myCollection.getAll({limit: 5, skip: 10})

#4 modify  data in a document - http://docs.appbase.io/#/v3.0/rest/api-reference#api-reference-document-properties-create-update-document-properties
error = myCollection.set('id', data) 
	#4.1 error is null if the operation succeeded

#remove property - http://docs.appbase.io/#/v3.0/rest/api-reference#api-reference-document-properties-delete-document-properties
myCollection.unset('id', 'propertyName')
myCollection.unset('id', ["property", "names"])

#5 delete a document - 
error = myCollection.delete('id')

#7 set a ref - http://docs.appbase.io/#/v3.0/rest/api-reference#api-reference-document-references-create-update-document-references
error = myCollection.setRef('id', 'ref name', "path", [priority])  
	# error is null if the operation succeeded

#7 get refs of a document - http://docs.appbase.io/#/v3.0/rest/api-reference#api-reference-document-references-read-references
arrayOfReferences = myCollction.getRefs('id')
  
  #6.1 filtering refs with a dictionary
  filters = {startAt: 5, limit: 10}
  arrayOfReferences = myCollection.getRefs('id', filters)

#8 delete a ref - http://docs.appbase.io/#/v3.0/rest/api-reference#api-reference-document-references-delete-references
error = myCollection.unsetRef('name')  
	# error is null if the operation succeeded

#9 listen (realtime)
#properties 
myCollection.on('id', callbackFunction)

#refs
myCollection.onRef('id', callbackFunction)

#creation/removal of documents in the whole collections
myCollection.onDocuments(callbackFunction)

#stop any callback from listening
myCollection.off(theSamecallbackFunction)
```

