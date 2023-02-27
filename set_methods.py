# set methods

print(list(filter(lambda x: not x.startswith("__"), dir(set))))

set1 = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}
print(f"set1: {set1}, len(set1): {len(set1)}")
set1.add("passion fruit")
set1.add("pineapple")
print(f"set1: {set1}")
set1.remove("apple")
print(f"set1: {set1}, len(set1): {len(set1)}")

help(set.union)
set2 = {"James", "Jerry", "John", "Jenny", "Jill", "cherry", "orange", "kiwi", "melon", "mango"}
# set1.difference_update(set2)
# print(f"set1: {set1}, len(set1): {len(set1)}")

union_set = set1.union(set2)  # set1 | set2
print(f"set1: {union_set}")
