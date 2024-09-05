## Caching
### Create a class BasicCache that inherits from BaseCaching and is a caching system:

Task 0:  You must use self.cache_data - dictionary from the parent class BaseCaching
This caching system doesn’t have limit
```python
def put(self, key, item):
```
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
```python
def get(self, key):
```
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.