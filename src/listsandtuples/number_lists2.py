empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

digits = list("432985617")
print(digits)

more_numbers = list(numbers)
more_numbers2 = numbers[:]
more_numbers3 = numbers.copy()
print(more_numbers)
print(numbers is more_numbers)
print(numbers == more_numbers)
print(more_numbers2)
print(numbers is more_numbers2)
print(numbers == more_numbers2)
print(more_numbers3)
print(numbers is more_numbers3)
print(numbers == more_numbers3)
