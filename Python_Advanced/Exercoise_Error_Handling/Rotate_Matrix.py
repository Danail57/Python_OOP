class MatrixContentError(Exception):
    pass

class MatrixSizeError(Exception):
    pass


def rotate_matrix(matrix):
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            raise MatrixSizeError("The size of the matrix is not a perfect square")


    for i in range(n):
        for j in range(n):
            value = matrix[i][j]
            try:
                matrix[i][j] = int(value)
            except ValueError:
                raise MatrixContentError("The matrix must consist of only integers")


    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
    return matrix

mtrx = []
while True:
    line = input()
    if not line:
        break
    mtrx.append(line.split())

try:
    rotated = rotate_matrix(mtrx)
    for row in rotated:
        print(*row)
except (MatrixContentError, MatrixSizeError) as err:
    print(err)
