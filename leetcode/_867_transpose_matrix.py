from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [list(item) for item in zip(*matrix)]

    def transpose2(self, matrix: List[List[int]]) -> List[List[int]]:
        row_size = len(matrix)
        col_size = len(matrix[0])

        new_matrix = []
        for col_idx in range(col_size):
            row = []
            for row_idx in range(row_size):
                row.append(matrix[row_idx][col_idx])
            new_matrix.append(row)

        return new_matrix


if __name__ == "__main__":
    s = Solution()
    print(s.transpose([[1,2,3],[4,5,6],[7,8,9]]))
    print(s.transpose([[1,2,3],[4,5,6]]))
