class Matrix:
    # класс матриц, сложение и вывод
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = ''
        for i in enumerate(self.matrix):
            result += ' '.join(map(str, i[1])) + '\n'
        return result

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix):
            for i in range(len(self.matrix) - 1):
                for j in range(len(self.matrix) - 1):
                    self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return Matrix(self.matrix)
        else:
            return "Матрицы должны быть одного размера!"


ma = Matrix([[31, 1], [2, 5], [40, 10]])
print(ma)
ma_1 = Matrix([[1, 2], [4, 5], [4, 1]])
print(ma_1)
print(ma + ma_1)
ma_2 = Matrix([[1, 2], [4, 5], [4, 1], [2, 4]])
print(ma + ma_2)
