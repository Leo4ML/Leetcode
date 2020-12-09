'''
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

示例 1：
输入："abc"
输出：3
解释：三个回文子串: "a", "b", "c"

示例 2：
输入："aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
 
提示：
输入的字符串长度不会超过 1000 。
'''
from functools import lru_cache


class Solution:
    # 只能想到暴力解，滑动窗口长度n，每滑动一次就judege一次是否为回文串，虽ac但是效率很低；
    # 枚举每个子字符串时间复杂度为O(n^2),子字符串判断是否为回文时间复杂度为O(n)，总得时间复杂度为O(n^3)
    # def countSubstrings(self, s: str) -> int:
    #     n = 2
    #     res = 0
    #     while n <= len(s):
    #         for i in range(len(s)-n+1):
    #             if self.judge(s[i:i+n]):
    #                 res += 1
    #         n += 1
    #     return res+len(s)

    # def judge(self, ss):
    #     k = len(ss)
    #     mid = k//2
    #     if ss[:mid] == ss[k-1:k-mid-1:-1]:
    #         return True
    # 题解一，找出回文中心，再两边拓展判断是否为回文，时间复杂度为O(n^2)；回文中心有一个和两个
    # def countSubstrings(self, s: str) -> int:
    #     res = 0
    #     for i in range(len(s)):
    #         cur1 = i
    #         for j in range(2):
    #             if cur1+j<len(s):
    #                 cur2 = cur1+j
    #                 left = cur1
    #                 right = cur2
    #                 while left >= 0 and right < len(s):
    #                     if s[left] == s[right]:
    #                         res += 1
    #                         left -= 1
    #                         right += 1
    #                     else:
    #                         break
    #     return res
    #
    # 题解二，Manacher算法；
    # Manacher 算法是在线性时间内求解最长回文子串的算法
    # Manacher 算法也会面临「方法一」中的奇数长度和偶数长度的问题，它的处理方式是在所有的相邻字符中间
    # 插入 #，比如 abaaabaa 会被处理成 #a#b#a#a#a#b#a#a#，这样可以保证所有找到的回文串都是
    # 奇数长度的，以任意一个字符为回文中心，既可以包含原来的奇数长度的情况，也可以包含原来偶数长度的情况。
    # 假设原字符串为 S，经过这个处理之后的字符串为 s。我们用 f(i) 来表示以 s 的第 i 位为回文
    # 中心，可以拓展出的最大回文半径，那么 f(i) - 1 就是以 i 为中心的最大回文串长度 （想一想为什么）。
    # Manacher 算法依旧需要枚举 ss 的每一个位置并先假设它是回文中心，但是它会利用已经计算出来的状态来
    # 更新f(i)，而不是向「中心拓展」一样盲目地拓展。Manacher算法如何通过已经计算出的状态来更新
    # f(i) 呢？Manacher 算法要求我们维护「当前最大的回文的右端点 r_m以及这个回文右端点对应的回文中心i_m
    # 没看懂Manacher解法
    # 20200826，看懂了并且写出算法，耗时52ms，时间复杂度比中心拓展法快很多
    def countSubstrings(self, s: str) -> int:
        tmp = ['#']
        for i in s:
            tmp.append(i)
            tmp.append('#')
        news = ''.join(tmp)
        n = len(news)
        dp = [0]*n
        c, r, res = -1, -1, 0
        for i in range(n):
            if i > r:
                dp[i] = 1
            else:
                dp[i] = min((r-i)*2+1, dp[2*c-i])
            left = i-dp[i]//2
            right = i+dp[i]//2
            while left-1 >= 0 and right+1 < n and news[left-1] == news[right+1]:
                left -= 1
                right += 1
                dp[i] += 2
            if i+(dp[i]-1)//2 > r:
                r = i+dp[i]//2
                c = i
        for i in dp:
            res += (i//2+1)//2
        return res
    # 题解三，动态规划
    # 有时我们想到动态规划，但又不知从何入手，可以试试这么思考：
    # 大问是什么？
    # 规模小一点的子问题是什么？
    # 它们之间有什么联系？
    # 大问题是一个字符串是否是回文串，那规模小一点的子问题呢？
    # 一个字串是回文串，它的首尾字符相同，且剩余子串也是一个回文串。
    # 罗列一下dp[i][j]为 true 的情形：
    # 1.由单个字符组成。（base case）
    # 2.由 2 个字符组成，且字符要相同。
    # 3.由多于 2 个字符组成，首尾字符相同，且剩余子串是一个回文串。
    # 时间复杂度：O(n^2)空间复杂度：O(n^2)
    # 状态转转移方程dp[i][j]=dp[i+1][j-1]&&s[i]==s[j]
    # def countSubstrings(self, s: str) -> int:
    #     res = 0
    #     n = len(s)
    #     dp = [[False] * n for _ in range(n)]
    #     for j in range(n):
    #         for i in range(j+1):
    #             if j-i == 0:
    #                 dp[i][j] = True
    #                 res += 1
    #             elif j-i==1 and s[j] == s[i]:
    #                 dp[i][j] = True
    #                 res += 1
    #             elif j-i>1 and dp[i+1][j-1] and s[j] == s[i]:
    #                 dp[i][j] = True
    #                 res += 1
    #     return res
s = Solution()
ss = 'aaaa'
print(s.countSubstrings(ss))
