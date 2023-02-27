# first we need to print the usable methods from the dictionary
print(list(filter(lambda x: not x.startswith("__"), dir(dict))))

# clear example
help(dict.clear)
d = {"name": "John", "age": 36}
print(f"d: {d}")
d.clear()
print(f"d: {d}")

# copy example
help(dict.copy)
d = {"name": "John", "age": 36, "address": {"city": "New York", "state": "NY"}}
d2 = d.copy()
print(f"d: {d}, d2: {d2}")
d2["name"] = "James"
# observe the difference
d2["address"]["city"] = "Los Angeles"
# d2["address"] = {"city": "Los Angeles", "state": "CA"}
d["age"] = 37
print(f"d: {d}, d2: {d2}")

# fromkeys example
help(dict.fromkeys)
d = dict.fromkeys(["name", "age", "address"], "unknown")
print(f"d: {d}")

# get example
help(dict.get)
d = {"name": "John", "age": 36}
print(f"d: {d}")
print(f"d.get('name'): {d.get('name')}")

print(f"get('address'): {d.get('address', 'unknown')}")
# get saves us the trouble of writing code like this:
if "address" in d:
    print(f"d['address']: {d['address']}")
else:
    print("d['address']: unknown")

# items example
help(dict.items)
d = {"name": "John", "age": 36}
print(f"d: {d}")
print(f"d.items(): {d.items()}")
for key, value in d.items():
    print(f"{key}: {value}")
d = {"James": "Bond", "John": "Doe", "Jane": "Doe", "Jill": "Doe", "Jerry": "Seinfeld", "Lucas": "Benjamin",
     "Luke": "Skywalker", "Leia": "Skywalker", "Han": "Solo", "Chewbacca": "Doe", "Obi-Wan": "Kenobi"}
# print all the values that are not Doe from the keys that do not start with J
for key, value in d.items():
    if not key.startswith("J") and value != "Doe":
        print(f"{key}: {value}", end=" | ")
print()

for key in d:
    if not key.startswith("J") and d[key] != "Doe":
        print(f"{key}: {d[key]}", end=" | ")
print()

# keys example
help(dict.keys)
d = {"name": "John", "age": 36}
print(f"d: {d}")
print(f"d.keys(): {d.keys()}")
for key in d.keys():  # this is the exact same thing as doing "for key in d:"
    print(f"{key}: {d[key]}")

# values example
help(dict.values)
d = {"name": "John", "age": 36}
print(f"d: {d}")
print(f"d.values(): {d.values()}")
for value in d.values():
    print(f"{value}")

# pop example
help(dict.pop)
d = {"name": "John", "age": 36}
print(f"d: {d}")
print(f"d.pop('name'): {d.pop('name')}")
print(f"d: {d}")

# popitem example, just like pop of last key!!
help(dict.popitem)
d = {"name": "John", "age": 36}
print(f"d: {d}")
print(f"d.popitem(): {d.popitem()}")
print(f"d: {d}")

# setdefault example
help(dict.setdefault)
d = {"name": "John", "age": 36}
print(f"d: {d}")
print(f"d.setdefault('name'): {d.setdefault('name')}")
print(f"d: {d}")
print(f"d.setdefault('address'): {d.setdefault('address', {'city': 'New York', 'state': 'NY'})}")
print(f"d: {d}")

# update example
help(dict.update)
d = {"name": "John", "age": 36}
print(f"d: {d}")
d.update({"name": "James", "age": 37})
print(f"d: {d}")
d.update({"address": {"city": "New York", "state": "NY"}})
print(f"d: {d}")
# replace a key with a new key but keep the value!!
name = d["name"]
del d['name']
d['name_long'] = name
print(f"d: {d}")
