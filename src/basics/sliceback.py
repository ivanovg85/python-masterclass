letters = "abcdefghigklmnopqrstuvwxyz"

backwards = letters[::-1]
print(backwards)

# slice the string to produce qpo
print(letters[16:13:-1])

# slice the string to produce edcba
print(letters[-22::-1])

# slice the string to produce the last 8 characters, in reverse order
print(letters[:-9:-1])

print(letters[-4:])
print(letters[-1:])
print(letters[:1])
print(letters[0])
