d3 = {1: 1, 2: 2.0, 3.0: "3", "4": 4, True: "True", None: "whatever", "James": "Bond", (1, 2, 3): "tuple"}
print(f"d3: {d3}, len(d3): {len(d3)}")

# extracting values from a dictionary
print(f"d3[1]: {d3[1]}, d3[2]: {d3[2]}, d3[3.0]: {d3[3.0]}, d3['4']: {d3['4']}, d3['James']: {d3['James']}")
print(f"d3[(1,2,3)]: {d3[(1, 2, 3)]}")

d4 = {True: 1, False: 7, 1: "This is new True", 0: "This is new False"}
print(d4)

d1 = {1: "one", 2: "two"}
# adding a new key-value pair to a dictionary
d1[3] = "three"  # add a new key-value pair
d1[4] = "four"
print(d1)
# also delete
del d1[1]  # delete a key-value pair
print(d1)

print("Iterating over a dictionary using a for loop:")
for k in d1:
    print(f"key: {k}, value: {d1[k]}")

print(f"1 in d1: {1 in d1}, 2 in d1: {2 in d1} and its value is {d1[2]}")  # False, True


