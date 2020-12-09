'''
在代号为 C-137 的地球上，Rick 发现如果他将两个球放在他新发明的篮子里，
它们之间会形成特殊形式的磁力。Rick 有 n 个空的篮子，第 i 个篮子的位置
在 position[i] ，Morty 想把 m 个球放到这些篮子里，使得任意两球间 最小磁力 最大。
已知两个球如果分别位于 x 和 y ，那么它们之间的磁力为 |x - y| 。
给你一个整数数组 position 和一个整数 m ，请你返回最大化的最小磁力。

示例 1：
输入：position = [1,2,3,4,7], m = 3
输出：3
解释：将 3 个球分别放入位于 1，4 和 7 的三个篮子，两球间的磁力分别
为 [3, 3, 6]。最小磁力为 3 。我们没办法让最小磁力大于 3 。

示例 2：
输入：position = [5,4,3,2,1,1000000000], m = 2
输出：999999999
解释：我们使用位于 1 和 1000000000 的篮子时最小磁力最大。
 
提示：
n == position.length
2 <= n <= 10^5
1 <= position[i] <= 10^9
所有 position 中的整数 互不相同 。
2 <= m <= position.length
'''
from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        gap = (position[-1]-position[0])/(m-1)
        res = position[-1]-position[0]
        last = position[0]
        cur = 0
        c = 1
        while c < m:
            tmp = last + gap
            while cur < len(position) and position[cur] < tmp:
                cur += 1
            if cur == len(position):
                res = min(res,position[-1]-last)
                c += 1
                break
            if position[cur] == tmp:
                res = min(res, tmp-last)
                last = position[cur]
            elif position[cur] > tmp:
                if tmp-position[cur-1] <= position[cur]-tmp and last!=position[cur-1]:
                    res = min(res, position[cur-1]-last)
                    last = position[cur-1]
                    cur -= 1
                else:
                    res = min(res, position[cur]-last)
                    last = position[cur]
            c += 1
        return int(res)

s = Solution()
position = [4784,9049,3151,7537,2734,1287,2875,6770,9565,6254,6898,2509,6583]
m = 13
print(s.maxDistance(position, m))
