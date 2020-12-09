'''
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
示例:
输入: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
输出: 4
'''

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        res = 1
        visited = []
        new = [[0 for _ in matrix[0]] for _ in matrix]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                new[i][j] = int(matrix[i][j])
        tmp = [s[:] for s in new[:]]
        tmp2 = [sum(s) for s in tmp]
        area = sum(tmp2)
        if area==0 or not matrix:
            return 0
        def check(x, y):
            d = 1
            area = 1
            while x+d < len(new) and y+d < len(new[0]) and new[x+d][y] == 1 and new[x][y+d] == 1:
                d += 1
            tmp = [s[y:y+d] for s in new[x:x+d]]
            tmp2 = [sum(s) for s in tmp]
            area = sum(tmp2)
            while area != d**2:
                d-=1
                tmp = [s[y:y+d] for s in new[x:x+d]]
                tmp2 = [sum(s) for s in tmp]
                area = sum(tmp2)
            return area
        for i in range(len(new)):
            for j in range(len(new[0])):
                if new[i][j] == 1 and (i,j) not in visited:
                    res = max(res, check(i, j))
        return res

s = Solution()
matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
print(s.maximalSquare(matrix))
