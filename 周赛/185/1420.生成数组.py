'''
给你三个整数 n、m 和 k 。下图描述的算法用于找出正整数数组中最大的元素。
maximum_value = -1
maximum_index = -1
search_cost = 0
n = arr.length
for (i = 0; i < n; i++){
    if (maximum_value < arr[i]){
        maximum_value = arr[i]
        maximum_index = i
        search_cost = search_cost + 1
    }
}
return maximum_index
请你生成一个具有下述属性的数组 arr ：

arr 中有 n 个整数。
1 <= arr[i] <= m 其中 (0 <= i < n) 。
将上面提到的算法应用于 arr ，search_cost 的值等于 k 。
返回上述条件下生成数组 arr 的 方法数 ，由于答案可能会很大，所以 必须 对 10^9 + 7 取余。

示例 1：
输入：n = 2, m = 3, k = 1
输出：6
解释：可能的数组分别为 [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]

示例 2：
输入：n = 5, m = 2, k = 3
输出：0
解释：没有数组可以满足上述条件

示例 3：
输入：n = 9, m = 1, k = 1
输出：1
解释：可能的数组只有 [1, 1, 1, 1, 1, 1, 1, 1, 1]

示例 4：
输入：n = 50, m = 100, k = 25
输出：34549172
解释：不要忘了对 1000000007 取余

示例 5：
输入：n = 37, m = 17, k = 7
输出：418930126

提示：
1 <= n <= 50
1 <= m <= 100
0 <= k <= n
'''
# 设 dp[n][i][k]dp[n][i][k] 为长度为 n，最大值为 i，search_cost 为 k 的数组的数目，则∑{m, i=1}dp[n][i][k] 即为所求．

# 边界条件 dp[0][i][k] = dp[n][0][k] = dp[n][i][0] = 0, dp[1][i][1] = 1，对于其它的 n, i, k分两种情况考虑：

# 当最大值 i 恰好只出现在数组末尾时，构造的方法有  ∑{i-1, j=1}dp[n−1][j][k−1] 种，即前 n-1 个元素都小于 i；

# 而当最大值出现在前 n-1 个元素之中时，数组末尾的元素可以从 1 到 i 中任意选取，即有 i * dp[n-1][i][k]种构造方法．

# 综上所述，有

# dp[n][i][k] = i*dp[n-1][i][k] + ∑{i-1, j=1}dp[n−1][j][k−1]

# 代码：

class Solution:
    def f(self, n, i, k):
        if (self.tmp[n][i][k] != -1):
            return self.tmp[n][i][k]
        if n == 0 or k == 0 or i == 0:
            self.tmp[n][i][k] = 0
            return 0
        if n == 1 and k == 1:
            self.tmp[n][i][k] = 1
            return 1
        r=0
        for j in range(1, i):
            r += self.f(n-1, j, k-1)
            r %= 1000000007
        r += self.f(n-1, i, k)*i
        r %= 1000000007
        self.tmp[n][i][k] = r
        return r
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        self.tmp = [[[-1 for t in range(k+1)] for j in range(m+1)] for i in range(n+1)]
        r = 0
        for i in range(1, m+1):
            r += self.f(n, i, k)
            r %= 1000000007
        return r
