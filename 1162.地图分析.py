'''
你现在手里有一份大小为 N x N 的「地图」（网格） grid，上面的每个「区域」（单元格）都用 0 和 1 标记好了。
其中 0 代表海洋，1 代表陆地，请你找出一个海洋区域，这个海洋区域到离它最近的陆地区域的距离是最大的。
我们这里说的距离是「曼哈顿距离」（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个区域之间的距离
是 |x0 - x1| + |y0 - y1| 。

如果我们的地图上只有陆地或者海洋，请返回 -1。

示例 1：
输入：[[1,0,1],[0,0,0],[1,0,1]]
输出：2
解释： 
海洋区域 (1, 1) 和所有陆地区域之间的距离都达到最大，最大距离为 2。
示例 2：
输入：[[1,0,0],[0,0,0],[0,0,0]]
输出：4
解释： 
海洋区域 (2, 2) 和所有陆地区域之间的距离都达到最大，最大距离为 4。

提示：
1 <= grid.length == grid[0].length <= 100
grid[i][j] 不是 0 就是 1
'''

from typing import List
from collections import deque


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = [[0]*col for _ in range(row)]
        count = 0
        queue = deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    queue.appendleft((i, j))
                    visited[i][j] = 1
        if not queue or len(queue) == row*col:
            return -1
        dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        while queue:
            n = len(queue)
            for _ in range(n):
                x, y = queue.pop()
                for dx, dy in dirs:
                    newx = x+dx
                    newy = y+dy
                    if newx < 0 or newx >= row or newy < 0 or newy >= col or visited[newx][newy] == 1:
                        continue
                    queue.appendleft((newx, newy))
                    visited[newx][newy] = 1
            count += 1
        return count-1


s = Solution()
grid = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
print(s.maxDistance(grid))
