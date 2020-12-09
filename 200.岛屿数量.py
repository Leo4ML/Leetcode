'''
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向
或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

示例 1:
输入:
11110
11010
11000
00000
输出: 1
示例 2:
输入:
11000
11000
00100
00011
输出: 3
'''
from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        queue = deque()
        row, col = len(grid), len(grid[0])
        dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    queue.appendleft((i, j))
                grid[i][j] = '-1'
                if queue:
                    count += 1
                    while queue:
                        n = len(queue)
                        for _ in range(n):
                            x, y = queue.pop()
                            for dx, dy in dirs:
                                newx = x+dx
                                newy = y+dy
                                if newx < 0 or newx >= row or newy < 0 or newy >= col or grid[newx][newy] == '-1' or grid[newx][newy] == '0':
                                    continue
                                queue.appendleft((newx, newy))
                                grid[newx][newy] = '-1'
        return count


class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        queue = deque()
        row = len(grid)
        col = len(grid[0])
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    queue.appendleft((i, j))
                grid[i][j] = '-1'
                if queue:
                    count += 1
                    while queue:
                        n = len(queue)
                        for _ in range(n):
                            x, y = queue.pop()
                            for dx, dy in dirs:
                                if x+dx >= row or x+dx < 0 or y+dy < 0 or y+dy >= col or grid[x+dx][y+dy] =='-1' or grid[x+dx][y+dy] != '1':
                                    continue
                                queue.appendleft((x+dx, y+dy))
                                grid[x+dx][y+dy] = '-1'
        return count


s = Solution()
ss = Solution2()
grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
#print(s.numIslands(grid))
print(ss.numIslands(grid))
