'''
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下
移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入
方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

示例 1：
输入：m = 2, n = 3, k = 1
输出：3
示例 1：
输入：m = 3, n = 1, k = 0
输出：1
提示：

1 <= n,m <= 100
0 <= k <= 20
'''


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        count = 0
        tmp = []
        for i in range(m):
            for j in range(n):
                if i//100+i % 100//10+i % 10+j//100+j % 100//10+j % 10 <= k:
                    tmp.append([i, j])

        def surround(x, y):
            tmp = [[x-1, y-1], [x, y-1], [x+1, y-1], [x-1, y],
                   [x+1, y], [x-1, y+1], [x, y+1], [x+1, y+1]]
            tmp2 = []
            for dot in tmp:
                if dot[0] < 0 or dot[0] >= m:
                    continue
                elif dot[1] < 0 or dot[1] >= n:
                    continue
                else:
                    tmp2.append(dot)
            return tmp2
        tmp3 = [[0, 0]]
        for dot in tmp[1:]:
            tmp2 = surround(dot[0], dot[1])
            for i in tmp2:
                if i in tmp3:
                    count += 1
                    if dot not in tmp3:
                        print('添加点', dot)
                        tmp3.append(dot)
                    break
            print('点周围的存在点为：', tmp2)
            print('tmp3为', tmp3)
        return count+1, tmp, tmp3


s = Solution()
r, tmp, tmp3 = s.movingCount(16, 8, 4)
print(r)
print(tmp)
print(tmp3)
