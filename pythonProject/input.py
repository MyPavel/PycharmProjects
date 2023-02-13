d = input()
print(d)
e = input('enter e ')
print (e)
a, b, c = [input('enter number ') for _ in range(3)]
print (a)
print (b)
print (c)
f, g, h = input('Enter 3 numbers ').split()
print (f)
print (g)
print (h)
t, y, u = map(int, input('Enter 3 numbers ').split()) # Ввод целых чисел
print (t, y, u, end=" ")