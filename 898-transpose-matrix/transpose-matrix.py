class Solution(object):
    def transpose(self, matrix):

        rows, columns = len(matrix), len(matrix[0])
        list = []

        for i in range(columns):
            list.append([0] * rows)

        for i in range(rows):
            for j in range(columns):
                list[j][i] = matrix[i][j] 

        return list