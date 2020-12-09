'''
厨房里总共有 n 个橘子，你决定每一天选择如下方式之一吃这些橘子：
吃掉一个橘子。
如果剩余橘子数 n 能被 2 整除，那么你可以吃掉 n/2 个橘子。
如果剩余橘子数 n 能被 3 整除，那么你可以吃掉 2*(n/3) 个橘子。
每天你只能从以上 3 种方案中选择一种方案。
请你返回吃掉所有 n 个橘子的最少天数。

示例 1：
输入：n = 10
输出：4
解释：你总共有 10 个橘子。
第 1 天：吃 1 个橘子，剩余橘子数 10 - 1 = 9。
第 2 天：吃 6 个橘子，剩余橘子数 9 - 2*(9/3) = 9 - 6 = 3。（9 可以被 3 整除）
第 3 天：吃 2 个橘子，剩余橘子数 3 - 2*(3/3) = 3 - 2 = 1。
第 4 天：吃掉最后 1 个橘子，剩余橘子数 1 - 1 = 0。
你需要至少 4 天吃掉 10 个橘子。

示例 2：
输入：n = 6
输出：3
解释：你总共有 6 个橘子。
第 1 天：吃 3 个橘子，剩余橘子数 6 - 6/2 = 6 - 3 = 3。（6 可以被 2 整除）
第 2 天：吃 2 个橘子，剩余橘子数 3 - 2*(3/3) = 3 - 2 = 1。（3 可以被 3 整除）
第 3 天：吃掉剩余 1 个橘子，剩余橘子数 1 - 1 = 0。
你至少需要 3 天吃掉 6 个橘子。

示例 3：
输入：n = 1
输出：1

示例 4：
输入：n = 56
输出：6

提示：
1 <= n <= 2*10^9
'''


class Solution:
    # @lru_cache(None)
    def minDays(self, n: int) -> int:
        # 方法一：
        # 将中间计算结果保存在字典，计算前查询是否有该结果，有则直接获取，无则min一下
        # 相比方法二，又避免了一些重复性计算
        # 1）带存储结果,输出字典种的结果
        # days = {'0': 0, '1': 1}
        # self.getAns(n, days)
        # print(days)
        # return days[str(n)]
        # 2）带存储结果，直接输出最后的结果，不从字典获取
        # days = {'0': 0, '1': 1}
        # return self.getAns(n, days)
        # 方法二：
        # 不需要另外的函数，直接递归(leetcode平台会TLE)
        # 如果采用缓存装饰器则不会TLE，即在方法前加上一行@lru_cache(None)
        # 依然存在部分重复计算比如n==18时，会重复计算n=3的情况
        if n<=1:
            return n
        return 1+min(self.minDays(n//2)+(n%2), self.minDays(n//3)+(n%3))

    def getAns(self, n, dic):
        mins = n
        if str(n) in dic:
            return dic[str(n)]
        mins = min(mins, self.getAns(n//2, dic)+(n % 2))
        mins = min(mins, self.getAns(n//3, dic)+(n % 3))
        mins += 1
        dic[str(n)] = mins
        return mins
    # 最初的解法也是先到dp，但是这种dp方法将每一种n全部计算一次，很容易出现TLE，
    # 而实际计算时，有很多无效的n存在
    # 比如n=16时，只需要计算n=1,2,3,5,8,16;
    # n=32时，仅需计算n=1,2,3,4,5,8,10,16,32.
    # 大大节约了时间（答案集中会测试n=89084693）
    # def minDays(self, n: int) -> int:
    #     dp = [0, 1, 2, 2]
    #     i = 4
    #     while i <= n:
    #         tmp = n
    #         if i % 2 == 0 and i % 3 == 0:
    #             tmp = min(tmp, dp[i-1]+1, dp[i//2]+1, dp[i//3]+1)
    #         elif i % 2 == 0 and i % 3 != 0:
    #             tmp = min(tmp, dp[i-1]+1, dp[i//2]+1)
    #         elif i % 2 != 0 and i % 3 == 0:
    #             tmp = min(tmp, dp[i-1]+1, dp[i//3]+1)
    #         else:
    #             tmp = min(tmp, dp[i-1]+1)
    #         dp.append(tmp)
    #         i+=1
    #     return dp[n]


s = Solution()
n = 89084693
print(s.minDays(n))
