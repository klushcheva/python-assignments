class MatrixSizeError(Exception):
    pass


class Matrix:
    def __init__(self, matrix):
        if not isinstance(matrix, list):
            raise TypeError("Argument must be a list")
        self.matrix = matrix

    def __str__(self) -> str:
        return "\n".join("\t".join(str(x) for x in row) for row in self.matrix)

    def __eq__(self, other) -> bool:
        """
        other: Matrix
        """
        if not isinstance(other, Matrix):
            return False
        return self.matrix == other.matrix

    def size(self) -> tuple:
        return len(self.matrix), len(self.matrix[0])

    def __add__(self, other) -> "Matrix":
        """
        other: Matrix
        """
        if not isinstance(other, Matrix):
            raise TypeError("Argument must be a Matrix object")
        if self.size() != other.size():
            raise MatrixSizeError("Matrices must have the same size")
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in
                  range(len(self.matrix))]
        return Matrix(result)

    def __sub__(self, other) -> "Matrix":
        """
        other: Matrix
        """
        if not isinstance(other, Matrix):
            raise TypeError("Argument must be a Matrix object")
        if self.size() != other.size():
            raise MatrixSizeError("Matrices must have the same size")
        result = [[self.matrix[i][j] - other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in
                  range(len(self.matrix))]
        return Matrix(result)

    def __mul__(self, other) -> "Matrix":
        """
        other: Matrix
        """
        if isinstance(other, Matrix):
            if self.size()[1] != other.size()[0]:
                raise MatrixSizeError(
                    "Number of columns of first matrix must be equal to number of rows of second matrix")
            result = [[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(other.matrix))) for j in
                       range(len(other.matrix[0]))] for i in range(len(self.matrix))]
            return Matrix(result)
        elif isinstance(other, (int, float)):
            result = [[self.matrix[i][j] * other for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
            return Matrix(result)
        else:
            raise TypeError("Argument must be a number or a Matrix object")

    def transpose(self) -> "Matrix":
        result = [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]
        return Matrix(result)

    def tr(self) -> float:
        if len(self.matrix) != len(self.matrix[0]):
            raise MatrixSizeError("Matrix must be square")
        return sum(self.matrix[i][i] for i in range(len(self.matrix)))

    def det(self) -> float:
        if len(self.matrix) != len(self.matrix[0]):
            raise MatrixSizeError("Matrix must be square")
        if len(self.matrix) == 1:
            return self.matrix[0][0]
        elif len(self.matrix) == 2:
            return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
        else:
            result = 0
            for i in range(len(self.matrix)):
                submatrix = [[self.matrix[j][k] for k in range(len(self.matrix)) if k != i] for j in
                             range(1, len(self.matrix))]
                result += ((-1) ** i) * self.matrix[0][i] * Matrix(submatrix).det()
            return result