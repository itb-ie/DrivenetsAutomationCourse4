list1 = list(range(0, 100))
print(list1)

print(f"all= {all(list1)}, False because list1[0]={list1[0]}")
print(f"any= {any(list1)}")

list1[0] = 100
print(f"all= {all(list1)}")

print("some odd/even examples!")
nums = [0, 2, 4, 12, 32, 99, 102]
# 2 steps:
true_false_even = list(num % 2 == 0 for num in nums)
print(true_false_even)
all_even = all(true_false_even)

# vs 1 step
any_odd = any(num % 2 for num in nums)

print(f"all_even = {all_even}")
print(f"at least one odd = {any_odd}")
