numbers = [0, 1, 2, 3, 4]
doubled_numbers = []
# without list comprehension
for num in numbers:
    doubled_numbers.append(num * 2)

print(doubled_numbers)

# using list comprehension

doubled_numbers = [num * 2 for num in numbers]

print(doubled_numbers)

friend_ages = [22, 31, 35, 37]
age_strings = ["My friend is {} years old.".format(age) for age in friend_ages]
print(age_strings)

odds = [age for age in friend_ages if age % 2 == 1]
