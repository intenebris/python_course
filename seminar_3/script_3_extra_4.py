def spiral_matrix(n):
    # Создаем матрицу размером n x n
    matrix = [[0] * n for _ in range(n)]

    # Индексы начальной точки
    x, y = 0, 0

    # Значения для заполнения матрицы
    values = list(range(1, n**2 + 1))

    # Количество элементов, которые нужно поместить в текущий квадрат
    size = n

    # Заполняем первый квадрат
    for i in range(size):
        matrix[x][y] = values.pop(0)
        x += 1

    # Переходим к следующему квадрату
    for i in range(n - 1):
        # Перемещаемся вниз
        for j in range(size - 1):
            matrix[x][y] = values.pop(0)
            y += 1
        # Перемещаемся влево
        for j in range(size - 1):
            matrix[x][y] = values.pop(0)
            x -= 1
        # Перемещаемся вверх
        for j in range(size - 1):
            matrix[x][y] = values.pop(0)
            y -= 1
        # Перемещаемся вправо
        for j in range(size - 1):
            matrix[x][y] = values.pop(0)
            x += 1

    return matrix
# Пример вывода для n=5
print(spiral_matrix(5))