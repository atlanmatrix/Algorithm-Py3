import math


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_size = math.floor(len(matrix) / 2)
        col_size = math.ceil(len(matrix) / 2)

        for row_idx in range(row_size):
            for col_idx in range(col_size):
                tmp = matrix[row_idx][col_idx]
                matrix[row_idx][col_idx] = matrix[-1 - col_idx][row_idx]
                matrix[-1 - col_idx][row_idx] = matrix[-1 - row_idx][-1 - col_idx]
                matrix[-1 - row_idx][-1 - col_idx] = matrix[col_idx][-1 - row_idx]
                matrix[col_idx][-1 - row_idx] = tmp

    def rotate2(self, matrix: list[list[int]]) -> list:
        """
        Do not return anything, modify matrix in-place instead.
        """
        try:
            row_size = len(matrix)
            col_size = len(matrix[0])

            # Create empty matrix
            rotated_matrix = []

            for col_idx in range(col_size):
                row_lst: list = []
                for row_idx in range(row_size):
                    row_lst.insert(0, matrix[row_idx][col_idx])
                rotated_matrix.append(row_lst)
            for i in range(row_size):
                matrix[i] = rotated_matrix[i]
            return rotated_matrix

        except IndexError:
            return []


if __name__ == "__main__":
    s = Solution()
    l = [[1,2,3],[4,5,6],[7,8,9]]
    s.rotate2(l)
    print(l)

    l = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    s.rotate2(l)
    print(l)
