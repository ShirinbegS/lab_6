# Функция для проверки, является ли число простым
def f(x):
    for i in range(2, x//2+1):
        if x % i == 0:
            return False
    return True
# Нахождение и вывод простых чисел с их порядковыми номерами
count = 0
for num in range(245690, 245756 + 1):
    if f(num):
        count += 1
        print(count, num)
