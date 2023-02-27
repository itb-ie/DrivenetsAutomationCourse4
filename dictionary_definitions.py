d1 = {}  # empty dictionary (pay attention, this is not a set!)
print(f"d1={d1}, type(d1)={type(d1)}")
d2 = dict()  # empty dictionary, another way to create an empty dictionary
print(f"d2={d2}, type(d2)={type(d2)}")
print(f"d1 == d2: {d1 == d2}")  # True
print(f"d1 is d2: {d1 is d2}")  # False

d1 = {"one": "unu", "two": "doi", "three": "trei", "four": "patru", "five": "cinci", "six": "sase",
      "seven": "sapte", "eight": "opt", "nine": "noua", "ten": "zece"}
d2 = {"one": "ehad", "two": "shteim", "three": "shalosh", "four": "arba", "five": "hamisha", "six": "shisha",
      "seven": "sheva", "eight": "shmone", "nine": "tesha", "ten": "eser"}

#  this is a complex dictionary, with different types of keys and values
d3 = {1: 1, 2: 2.0, 3.0: "3", "4": 4, True: "True", None: "whatever", "James": "Bond", (1, 2, 3): "tuple"}
# but not something like this
# d4 = {[1, 2, 3]: "list", {1: 1, 2: 2}: 7}  # TypeError: unhashable type: 'list'

# lets combine d1 and d2 into a new dictionary
ro_to_hebrew = {}
hebrew_to_ro = {}
for k, v in d1.items():
    ro_to_hebrew[v] = d2[k]
    hebrew_to_ro[d2[k]] = v
print(ro_to_hebrew)
print(hebrew_to_ro)

