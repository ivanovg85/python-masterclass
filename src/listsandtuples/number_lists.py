even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

print(min(even))
print(max(even))
print(min(odd))
print(max(odd))

print()
print(len(even))
print(len(odd))

print()
print("mississippi".count("issi"))

print()
even.extend(odd)
print(even)
another_even = even
print(another_even)

even.sort()
print(even)

even.sort(reverse=True)
print(even)
print(another_even)
