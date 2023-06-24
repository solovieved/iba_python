# В матрице найти номер строки, сумма чисел в которой максимальна.

matrix = [
    [7, 8, 9],
    [1, 2, 3],
    [4, 5, 6]
]
max_sum = float('-inf')
max_sum_row = -1

for i, row in enumerate(matrix):
    row_sum = sum(row)
    if row_sum > max_sum:
        max_sum = row_sum
        max_sum_row = i

print("Номер строки с максимальной суммой чисел:", max_sum_row)
