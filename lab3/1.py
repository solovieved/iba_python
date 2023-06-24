def cut_rectangle(a, b):
    if a == 0 or b == 0:
        return []

    sides = []
    side = min(a, b)
    sides.append(side)

    if a > b:
        sides.extend(cut_rectangle(a - side, b))
    else:
        sides.extend(cut_rectangle(a, b - side))

    return sides


a = int(input("Введите сторону a прямоугольника: "))
b = int(input("Введите сторону b прямоугольника: "))
sides = cut_rectangle(a, b)

print("Длины ребер квадратов:", print(sides))
print("Количество квадратов:", len(sides))
