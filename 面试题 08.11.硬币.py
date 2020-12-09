'''
硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。
(结果可能会很大，你需要将结果模上1000000007)

示例1:
 输入: n = 5
 输出：2
 解释: 有两种方式可以凑成总金额:
5=5
5=1+1+1+1+1
示例2:
 输入: n = 10
 输出：4
 解释: 有四种方式可以凑成总金额:
10=10
10=5+5
10=5+1+1+1+1+1
10=1+1+1+1+1+1+1+1+1+1
说明：

注意:
你可以假设：
0 <= n (总金额) <= 1000000
'''

# dp[i][j]表示前i种硬币组成金额j的方法数；那么dp[1][j]代表只有1元硬币情况下j金额的组合数，即dp[1][j]=1；
# dp[i][j]=dp[i-1][j]+dp[i-1][j-vi]+dp[i-1][j-2*vi]...+dp[i-1][j-n*vi],vi表示第i种硬币的面值；
# dp[i][0]=1,不管多少种硬币组成金额0的方式只有1
import time

'''
# 超出时间限制
class Solution:
    def waysToChange(self, n: int) -> int:
        dp = [[0 for _ in range(n+1)]for _ in range(5)]
        for i in range(5):
            dp[i][0] = 1
        coins = [1, 5, 10, 25]
        for i in range(1, len(coins)+1):
            coin = coins[i-1]
            for j in range(1, n+1):
                for k in range(0, j//coin+1):
                    dp[i][j] += dp[i-1][j-k*coin]
        return dp[4][n] % 1000000007
'''


class Solution:
    def waysToChange(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        coins = [1, 5, 10, 25]
        for i in range(5):
            for j in range(coins[i], n+1):
                dp[j] += dp[j-coins[i]]
        return dp[n]


t1 = time.time()
s = Solution()
n = 5
print(s.waysToChange(n))
t2 = time.time()
print('%.2f' % (t2-t1))
