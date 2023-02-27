# there are two ways to define a tuple
tpl = (1, 2, 3, 4, 5)
tpl2 = tuple([(1, 2, 3), ("a", "b", "c"), (True, False, None, -1)])
# help(tuple)
print(f"The values of the first tuple are: {tpl}")
print(f"The values of the second tuple are: {tpl2}")
print(f"The type of the first tuple is: {type(tpl)}")
print(f"The type of the second tuple is: {type(tpl2)}")
tpl3 = tuple("Hello World")
print(f"The values of the third tuple are: {tpl3}")
print(f"The type of the third tuple is: {type(tpl3)}")
tpl4 = (1)  # this is not a tuple
tpl4 = (1,)  # this is a tuple of one element
list1 = [1]    # this is a list one 1 element
print(f"The values of the fourth tuple are: {tpl4}")
print(f"The type of the fourth tuple is: {type(tpl4)}")

