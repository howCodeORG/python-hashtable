A Hash Table written in Python
==============================

This repository includes the hmap module which is an implementation of a hash table in Python.

Also included is a demo.py script to showcase the hash table.

You can use the hash table by creating a new Map object, as shown below:
```python
myhashtable = Map()
```

You can insert values into the table using the put method from the Map class.
```python
myhashtable = Map()
myhashtable.put("my key", "my value")
```

You can retrieve values from the hash table using the get method from the Map class.
```python
myhashtable = Map()
myhashtable.put("my key", "my value")

myhashtable.get("my key") # returns "my value"
myhashtable.get("some key") # return None
```
