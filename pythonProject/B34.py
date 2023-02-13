# Задание 3.4.1
a = int(input('Введите целое число А'))
b = int(input('Введите целое число B'))
c = (a % 2 != 0) and (b % 2 != 0)
print('Значение С', c)

# Задание 3.4.2
d = int(input('Введите год от 1900 до 3000'))
if (d % 4 == 0) and (d % 100 != 0) or (d % 400 == 0):
    print(d, 'Високосный')
else:
    print(d, 'Обычный')


# Задание 3.4.3
def fun(x, y):
    if (x > 0) and (y > 0):
        print('First quarter')
    if (x < 0) and (y > 0):
        print('Second quarter')
    if (x < 0) and (y < 0):
        print('Third quarter')
    if (x > 0) and (y < 0):
        print('Fourth quarter')


# Задание 3.4.4
def get_wind_class(speed):  # Объявление функции
    if 1 < speed < 4:
        return "weak [1]"
    elif 5 <= speed <= 10:
        return "moderate [2]"
    elif 11 <= speed <= 18:
        return "strong [3]"
    elif 19 <= speed:
        return "hurricane [4]"


print(get_wind_class(3))  # Печатаем результат выполнения

# Задание 3.4.5
# Римские цифры

# Задание 3.4.6
# Сопоставление значений в словаре

# Задание 3.4.7
A = int(input('Enter A'))
B = int(input('Enter B'))
C = int(input('Enter C'))


def fun(A, B, C):
    if ((A < 45) and (B >= 45) and (C >= 45)) or \
            ((A >= 45) and (B < 45) and (C >= 45)) or \
            ((A >= 45) and (B >= 45) and (C < 45)):
        return "Есть число меньше 45 и только одно"
    else:
        return "Числа меньше 45 нет или их несколько"


print(fun(A, B, C))

# Задание 3.4.8
a = int(input('Enter digit\n'))


def fun(a):
    if (-10 < a < -1) or (2 < a < 15):
        return "Number belong to range"
    else:
        return "Number does not belong to range"


print(fun(A))

# Задание 3.4.9
x = int(input("Enter digit\n"))
def fun(x):
    if (10 <= x <= 99)and(x%5 == 0):
        return 'Five including in digit'
    else:
        return '5 none including or non-two-digit number'

print(fun(x))
# Задание 3.4.10
list_ = [-5, 2, 4, 8, 12, -7, 5]

print(len(list_) == len(set(list_)))
# Задание 3.4.11
num = input('Enter number')
print(str(num))
print(str(num)[::-1])
if str(num) != str(num)[::-1]:
    print (num, 'not polindrom')
else:
    print (num, 'polindrom')

# Итоговое задание (кривое, делал не я)
#Запрашиваем ввод температуры
temperature = int(input("Input temperature: "))

#для указания начальных статусов дождливости воспользуемся False или None
rainy = None
heavyRain = None

#если температура <0 то про дождь спрашивать бессмысленно
if temperature > 0:
   rainy = input("Is rainy: ") == "yes"
#если идет дождь спросим насколько он серьезный
   if rainy:
       heavyRain = input("Is heavy rain: ") == "yes"


#реализуем логику по схеме
decision = "Не решил что брать. Останусь дома."
if (temperature) > 20 and (temperature < 30) :
   if rainy:
       decision = "Взять футболку шорты и дождевик"
   else:
       decision = "Взять футболку и шорты"
elif temperature > 0:
   if rainy:
       if heavyRain:
           decision = "Взять пальто, резиновые сапоги и зонт"
       else:
           decision = "Взять пальто и дождевик"
   else:
       decision = "Взять пальто"
else:
   decision = "Взять пуховик"


#Выведем наше решение на экран
print(decision)