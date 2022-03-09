"""
write a program that would only print odd numbers, sorted in ascending order, from a given unsorted list.
"""

my_list = [13, 20, 11, 18, 3, 12, 0, 7, 9, 99, 44, 76]
# write a program that would only print odd numbers, sorted in ascending order, from a given unsorted list.

odd_list = []
for i in my_list:
    if i % 2 != 0:
        odd_list.append(i)  # append odd numbers to odd_list

# sorted odd_list
odd_list.sort()
print(odd_list)
