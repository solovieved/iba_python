import os

with open('F1.txt', 'r') as f1:
    lines = f1.readlines()

with open('F2.txt', 'w') as f2:
    even_lines = [line for i, line in enumerate(lines) if i % 2 == 1]
    f2.writelines(even_lines)

size_f1 = os.path.getsize('F1.txt')
size_f2 = os.path.getsize('F2.txt')

print(f"Размер файла F1: {size_f1}")
print(f"Размер файла F2: {size_f2}")
