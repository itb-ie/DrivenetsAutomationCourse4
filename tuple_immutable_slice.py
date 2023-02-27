tpl = (1, 2, 3, 4, 5)

# tuples are immutable, you can not change them
try:
    tpl[0] = 100
except TypeError as e:
    print(f"TypeError: {e}")

print(f"However you can slice tuples")
print(f"tpl[0:2]: {tpl[0:2]}")  # 1, 2
print(f"tpl[2:]: {tpl[2:]}")  # 3, 4, 5
print(f"tpl[:2]: {tpl[:2]}")  # 1, 2
print(f"tpl[::2]: {tpl[::2]}")  # 1, 3, 5
print(f"tpl[::-1]: {tpl[::-1]}")  # 5, 4, 3, 2, 1
print(f"tpl[::-2]: {tpl[::-2]}")  # 5, 3, 1

# what if I want to change the value of the first element of the tuple?
# I can not do it, but I can create a new tuple
tpl2 = (100, *tpl[1:])  # this is called tuple unpacking
tpl2 = (100, tpl[1], tpl[2], tpl[3], tpl[4])
print(f"tpl2: {tpl2}")
tpl3 = (100,) + tpl[1:]  # this is called tuple concatenation
print(f"tpl3: {tpl3}")




