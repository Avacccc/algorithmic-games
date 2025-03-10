class SparseMatrix:
    """
    A class for create and save matrices in sparse form.
    """

    def __init__(self):
        self.elements = []

    def set_value(self, row, col, value):
        """
        Set value for element in row = row and column = col.
        """
        if value != 0:
            self.elements.append([row, col, value])

    def get_value(self, row, col):
        """
        Get value of elements in row = row and column = col.
        """
        for r, c, v in self.elements:
            if r == row and c == col:
                return v

        return 0
    
    def update_value(self, row, col, new_value):
        """
        Updates the value of an existing element or adds a new element.
        """
        for i, (r, c, v) in enumerate(self.elements):
            if r == row and c == col:
                if new_value == 0:
                    self.elements.pop(i)
                else:
                    self.elements[i][2] = new_value
                return
        if new_value != 0:
            self.elements.append([row, col, new_value])    
    
    
    def row_count(self):
        """
        Number of rows.
        """
        row_size = self.elements[0][0]
        return row_size

    def col_count(self):
        """
        Number of Columns.
        """
        col_size = self.elements[0][1]
        return col_size

    def non_zero_count(self):
        """
        Number of non-zero elements in a matrix.
        """
        return len(self.elements)

    def size_check(self, other):
        """
        If two matrix are not same size return False.
        """
        if (self.row_count() == other.row_count()) and (self.col_count() == other.col_count()):
            return True
        return False

    def sum_1(self, other):
        """
        Adds two sparse matrices.
        """
        if not self.size_check(other):
            raise ValueError("Matrix dimensions do not match.")

        result = SparseMatrix()
        for r, c, v in self.elements:
            result.set_value(r, c, v)
        for r, c, v in other.elements:
            result.update_value(r, c, result.get_value(r, c) + v)
        return result

    def transpose(self):
        """
        Return transpose of a sparse matrix.
        """
        if not self.elements:
            return "Matrix is empty!!"

        transpose = SparseMatrix()
        for r, c, v in self.elements:
            transpose.set_value(c, r, v)
        return transpose
    
    def multiply(self, mat):
        if self.row_count != mat.col_count():
            return 'size dont match'
        result = SparseMatrix()
        for i in range(self.row_count()):
            for j in range(mat.col_count()):
                v = 0
                for k in range(self.col_count()):
                    v += self.get_value(i,k) * mat.get_value(k,j)
                result.set_value(i, j, v)
        return result

    def display(self):
        """
        Display sparse form.
        """
        col_size = self.col_count()
        row_size = self.row_count()
        non_zero = self.non_zero_count()
        print(f"row:{row_size + 1}   col:{col_size + 1}   n:{non_zero}")
        for r, c, v in self.elements:
            print(f"{r}       {c}       {v}", end="       ")
            print()

    def display_mat(self):
        """
        Display main matrix not sparse form.
        """
        col_size = self.col_count()
        row_size = self.row_count()
        mat = []
        for i in range(row_size + 1):
            mat.append([0] * (col_size + 1))
        for r, c, v in self.elements:
            mat[r][c] = v
        for j in mat:
            print(j)

def convertToSparseMatrix(matrix): 
    """
    converts normal matrix to sparse matrix
    """
    sparse = SparseMatrix()
    rows = len(matrix)
    cols = len(matrix[0])
    values = 0

    for i in range(len(matrix)): 
        for j in range(len(matrix[0])): 
            if matrix[i][j] != 0 : 
                sparse.set_value(i, j, matrix[i][j])
                values += 1

    sparse.elements.insert(0, [rows, cols, values])
    return sparse
