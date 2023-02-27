print(dir(tuple))
print("The actual usable methods are: ")
print(list(filter(lambda x: not x.startswith("__"), dir(tuple))))


help(tuple.count)
help(tuple.index)

tpl = (1, 2, 3, 4, 5, 1, 2, 4, 5, 1, 4, 5)
print(tpl.count(1), tpl.count(2), tpl.count(3))

print(tpl.index(1), tpl.index(2), tpl.index(3))
try:
    print(tpl.index(6))  # ValueError: tuple.index(x): x not in tuple
except ValueError as e:
    print(f"ValueError: {e}")

