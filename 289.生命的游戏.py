'''
根据 百度百科 ，生命游戏，简称为生命，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。

给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始
状态：1 即为活细胞（live），或 0 即为死细胞（dead）。每个细胞与其八个相邻位置（水平，
垂直，对角线）的细胞都遵循以下四条生存定律：

如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
根据当前状态，写一个函数来计算面板上所有细胞的下一个（一次更新后的）状态。下一个状态是通过
将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。
示例：

输入： 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
输出：
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
] 

进阶：

你可以使用原地算法解决本题吗？请注意，面板上所有格子需要同时被更新：你不能先更新某些格子，然后使
用它们的更新后的值再更新其他格子。
本题中，我们使用二维数组来表示面板。原则上，面板是无限的，但当活细胞侵占了面板边界时会造成问题。
你将如何解决这些问题？

'''
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def judge(x, y, board):
            row = len(board)
            col = len(board[0])
            surround = [[x-1, y-1], [x-1, y], [x-1, y+1], [x, y-1],
                        [x, y+1], [x+1, y-1], [x+1, y], [x+1, y+1]]
            live = 0
            death = 0
            for dot in surround:
                if dot[0] < 0 or dot[0] >= row:
                    continue
                if dot[1] < 0 or dot[1] >= col:
                    continue
                if board[dot[0]][dot[1]] == 0:
                    death += 1
                else:
                    live += 1
            if board[x][y] == 1:
                if live == 2 or live == 3:
                    return True
                else:
                    return False
            else:
                if live == 3:
                    return True
                else:
                    return False
        row = len(board)
        col = len(board[0])
        copyone = [[None for i in range(col)]for j in range(row)]
        for i in range(len(copyone)):
            for j in range(len(copyone[0])):
                copyone[i][j] = judge(i, j, board)
        for i in range(len(copyone)):
            for j in range(len(copyone[0])):
                if copyone[i][j]:
                    board[i][j] = 1 
                else:
                    board[i][j] = 0
        return board


s = Solution()
board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
print(s.gameOfLife(board))
