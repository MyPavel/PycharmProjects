# Пример 1
def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)
print(fact(3))
# Число Фибоначчи

def rec_fibb(n):
   if n == 1:
       return 1
   if n == 2:
      return 1
   return rec_fibb(n - 1) + rec_fibb(n - 2)

print(rec_fibb(10))  # 55

# 4.3.3
def rec_sum(n):
   if n == 1:  # терминальный случай
       return 1
   return n + rec_sum(n - 1)  # рекурсивный вызов

print(rec_sum(4))


# 4.3.4
def reverse_str(string):
   if len(string) == 0:
       return ''
   else:
       return string[-1] + reverse_str(string[:-1])

print(reverse_str('test'))  # tset

# 4.3.5

def sum_digit(n):
   if n < 10:
       return n
   else:
       return n % 10 + sum_digit(n // 10)

sum_digit(123)  # 6

# 5.4.9
def min_list(L):
    if len(L) == 1:
        return L[0]
    return L[0] if L[0] < min_list(L[1:]) else min_list(L[1:])
L = [i for i in 10]
print(min_list(L))

# 5.4.10
def mirror(a, res=0):
    return mirror(a // 10, res*10 + a % 10) if a else res

print(mirror(1234))
# Пояснение
a = 123456789
b = 0
while a:
    b = b * 10 + a % 10
    a = a // 10

print(b)