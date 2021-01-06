'''
给定一个整数矩阵，找出最长递增路径的长度。
对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。

示例 1:
输入: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
输出: 4 
解释: 最长递增路径为 [1, 2, 6, 9]。

示例 2:
输入: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
输出: 4 
解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
'''
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        maxpath = 0
        res = [[0] * len(matrix[0]) for _ in range(matrix)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = self.findMax(matrix, i, j)
                res[i][j] = res
                maxpath =  max(, maxpath)
        return maxpath

    def findMax(self, matrix, i, j):
        dire = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        queue = [(i, j)]
        c = 0
        while queue:
            c += 1
            for _ in range(len(queue)): 
                x, y = queue[0]
                visited = [(x, y)]
                for dx, dy in dire:
                    new_x = dx+x
                    new_y = dy+y
                    if (0 <= new_x < len(matrix)) and (0 <= new_y < len(matrix[0])):
                        if matrix[new_x][new_y] > matrix[x][y] and (new_x, new_y) not in visited:
                            queue.append((new_x, new_y))
                            visited.append((new_x, new_y))
                queue.pop(0)
        return c


nums = [
    [0,1,2,3,4,5,6,7,8,9],
    [19,18,17,16,15,14,13,12,11,10],
    [20,21,22,23,24,25,26,27,28,29],
    [39,38,37,36,35,34,33,32,31,30],
    [40,41,42,43,44,45,46,47,48,49],
    [59,58,57,56,55,54,53,52,51,50],
    [60,61,62,63,64,65,66,67,68,69],
    [79,78,77,76,75,74,73,72,71,70],
    [80,81,82,83,84,85,86,87,88,89],
    [99,98,97,96,95,94,93,92,91,90],
    [100,101,102,103,104,105,106,107,108,109],
    [119,118,117,116,115,114,113,112,111,110],
    [120,121,122,123,124,125,126,127,128,129],
    [139,138,137,136,135,134,133,132,131,130],
    [0,0,0,0,0,0,0,0,0,0]
    ]
s = Solution()
print(s.findMax(nums,2,1))
# print(s.longestIncreasingPath(nums))
