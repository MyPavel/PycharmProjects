s='hello'
print(s)
print(s[:1])
print(s[2:])
print(s[::2])
print(s[::3])
print(s[::-1])
print(len(s))
print(s.isalpha())

colors = 'red blue green'
colors_split = colors.split()
print(colors.split())
colors_joined = ' and '.join(colors_split)
print(colors_joined)