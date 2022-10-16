def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix[0])
        for row in range (n):
            for col in range(row,n):
                matrix[col][row], matrix[row][col]=matrix[row][col], matrix[col][row]
        for i in range(n):
            matrix[i].reverse()
