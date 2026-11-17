Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> class HashTable:
...     def __init__(self):
...         self.collection = {}
... 
...     def hash (self,key):
...         return sum(ord(char) for char in key)
...     
...     def add(self, key, value):
...         hashed_key = self.hash (key)
... 
...         if hashed_key not in self.collection:
...             self.collection[hashed_key] = {}
... 
...         self.collection[hashed_key][key] = value
... 
...     def remove (self, key):
...         hashed_key = self.hash(key)
... 
...         if hashed_key in self.collection:
...             if key in self.collection[hashed_key]:
...                 del self.collection[hashed_key][key]
... 
...     def lookup (self, key):
...         hashed_key = self.hash(key)
... 
...         if hashed_key in self.collection:
...             if key in self.collection[hashed_key]:
...                 return self.collection [hashed_key][key]
... 
