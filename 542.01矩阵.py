'''
给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。
两个相邻元素间的距离为 1 。
示例 1:
输入:

0 0 0
0 1 0
0 0 0
输出:

0 0 0
0 1 0
0 0 0
示例 2:
输入:

0 0 0
0 1 0
1 1 1
输出:

0 0 0
0 1 0
1 2 1
注意:
给定矩阵的元素个数不超过 10000。
给定矩阵中至少有一个元素是 0。
矩阵中的元素只在四个方向上相邻: 上、下、左、右。
'''
from collections import deque
from typing import List

# DFS/BFS

'''
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        r = [[999 for i in range(len(matrix[0]))]for j in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    r[i][j] = 0
                else:
                    if i-1 >= 0 and j-1 < 0:
                        r[i][j] = 1+r[i-1][j]
                    elif i-1 >= 0 and j-1 >= 0:
                        r[i][j] = 1+min(r[i-1][j], r[i][j-1])
                    elif i-1 < 0 and j-1 < 0:
                        continue
                    else:
                        r[i][j] = 1+r[i][j-1]
        for i in range(len(matrix)-1, -1, -1):
            for j in range(len(matrix[0])-1, -1, -1):
                if matrix[i][j] == 0:
                    r[i][j] = 0
                else:
                    if i+1 < len(matrix) and j+1 >= len(matrix[0]):
                        r[i][j] = min(1+r[i+1][j], r[i][j])
                    elif i+1 < len(matrix) and j+1 < len(matrix[0]):
                        r[i][j] = min(
                            1+min(r[i+1][j], r[i][j+1]), r[i][j])
                    elif i+1 >= len(matrix) and j+1 >= len(matrix[0]):
                        continue
                    else:
                        r[i][j] = min(1+r[i][j+1], r[i][j])
        return r
'''

# BFS方法
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        queue = deque()
        row, col = len(matrix), len(matrix[0])
        count = 0
        res=[[0]*col for _ in range(row)]
        visited=[[0]*col for _ in range(row)]
        dirs=[(0,-1),(-1,0),(0,1),(1,0)]
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    queue.appendleft((i, j))
                    visited[i][j]=1
        while queue:
            n=len(queue)
            for i in range(n):
                x,y = queue.pop()
                if matrix[x][y]==1:
                    res[x][y]=count
                for dx,dy in dirs:
                    newx=x+dx
                    newy=y+dy
                    if newx<0 or newx>=row or newy<0 or newy>=col or visited[newx][newy]==1:
                        continue
                    queue.appendleft((newx,newy))
                    visited[newx][newy]=1
            count+=1
        return res


s = Solution()
matrix = [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 0, 0, 0, 0, 1], [
    0, 0, 1, 0, 1, 1, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0, 1, 0], [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]]
print(s.updateMatrix(matrix))
