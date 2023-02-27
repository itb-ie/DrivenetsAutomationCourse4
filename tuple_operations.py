tpl1 = (1, "2", 3, -4, 5.5, "James", True, None, 1)
tpl2 = (6, 7, 8, 9, 10)
print(f"tpl1 + tpl2: {tpl1 + tpl2}")
print(f"tpl1 * 3: {tpl1 * 3}")
print(f"len(tpl1): {len(tpl1)}")

# tuples are iterable, you can iterate over them using a for loop
print("Iterating over a tuple using a for loop:")
print("| ", end="")
for item in tpl1:
    print(item, end=" | ")
print()

print("Unpacking a tuple:")
# tuple unpacking, tuples are great for switching values
a = 1
b = 2
b, a = a, b  # this is called tuple unpacking, same as writing: a, b = (b, a)
print(f"a: {a}, b: {b}")

# classic way of switching values, non pythonic
a = "first text"
b = "second text"
helper = b
b = a
a = helper
print(f"a: {a}, b: {b}")


