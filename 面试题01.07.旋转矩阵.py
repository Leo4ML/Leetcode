'''
给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。
不占用额外内存空间能否做到？

示例 1:

给定 matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
示例 2:
给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
'''
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row//2):
            for j in range(i, col-1-i):
                print(matrix[i][j], matrix[j][col-i-1], matrix[row-i-1][col-1-j], matrix[row-1-j][i])
                matrix[i][j], matrix[j][col-i-1], matrix[row-i-1][col-1-j], matrix[row-1-j][i] = \
                    matrix[row-1-j][i],matrix[i][j], matrix[j][col-i-1], matrix[row-i-1][col-1-j]
        return matrix


matrix = [[]]
s = Solution()
print(s.rotate(matrix))
