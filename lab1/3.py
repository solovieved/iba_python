# 10. Найти среднее арифметическое трех последних элементов списка.
import random

n = int(input("Введите размер списка: "))

if n < 3:
    print('Размер списка должен быть больше 2')
else:
    random_list = [random.randint(0, 99) for _ in range(n)]
    print("Список :", random_list)
    last_three = random_list[-3:]
    average = sum(last_three) / len(last_three)
    print("Среднее арифметическое трех последних элементов:", average)
