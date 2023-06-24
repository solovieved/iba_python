# 2. Введите одномерный целочисленный список. Найдите наибольший нечетный элемент.
# Найдите минимальный по модулю элемент списка.

lst = list(map(int, input("Введите список целых чисел через пробел: ").split()))

max_odd = float('-inf')
min_abs = float('inf')

for num in lst:
    if num % 2 != 0 and num > max_odd:
        max_odd = num

    if abs(num) < abs(min_abs):
        min_abs = num

if max_odd == float('-inf'):
    print("В списке нет нечетных элементов.")
else:
    print("Наибольший нечетный элемент:", max_odd)

print("Минимальный по модулю элемент:", min_abs)
