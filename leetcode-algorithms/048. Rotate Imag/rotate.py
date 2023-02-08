from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2):
            for j in range((1 + n) // 2):
                (
                    matrix[i][n - 1 - j],
                    matrix[n - 1 - j][n - 1 - i],
                    matrix[n - 1 - i][j],
                    matrix[j][i],
                ) = (
                    matrix[j][i],
                    matrix[i][n - 1 - j],
                    matrix[n - 1 - j][n - 1 - i],
                    matrix[n - 1 - i][j],
                )
        print(matrix)


s = Solution()
s.rotate(matrix=[[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])

