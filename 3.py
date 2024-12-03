# Функция для проверки, является ли число простым
def f(x):
    if x < 2:
        return False
    if x==2:
        return True
    if x%2==0:
        return False
    for i in range(2, int(x**0.5)+1, 2):
        if x % i == 0:
            return False
    return True
# Диапазон чисел
start = 245690
end = 245756

# Нахождение и вывод простых чисел с их порядковыми номерами
count = 0
for num in range(start, end + 1):
    if f(num):
        count += 1
        print(count, num)
