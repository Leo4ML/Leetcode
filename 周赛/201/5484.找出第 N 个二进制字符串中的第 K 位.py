'''
给你两个正整数 n 和 k，二进制字符串  Sn 的形成规则如下：
S1 = "0"
当 i > 1 时，Si = Si-1 + "1" + reverse(invert(Si-1))
其中 + 表示串联操作，reverse(x) 返回反转 x 后得到的字符串，而 invert(x) 则
会翻转 x 中的每一位（0 变为 1，而 1 变为 0）
例如，符合上述描述的序列的前 4 个字符串依次是：

S1 = "0"
S2 = "011"
S3 = "0111001"
S4 = "011100110110001"
请你返回  Sn 的 第 k 位字符 ，题目数据保证 k 一定在 Sn 长度范围以内。

 
示例 1：
输入：n = 3, k = 1
输出："0"
解释：S3 为 "0111001"，其第 1 位为 "0" 。

示例 2：
输入：n = 4, k = 11
输出："1"
解释：S4 为 "011100110110001"，其第 11 位为 "1" 。

示例 3：
输入：n = 1, k = 1
输出："0"

示例 4：
输入：n = 2, k = 3
输出："1"

提示：

1 <= n <= 20
1 <= k <= 2n - 1
'''


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        lo = [0, 1, 3]
        for i in range(3, n+1):
            lo.append(2*lo[i-1]+1)
        return self.getK(lo, n, k, 0)

    def getK(self, lo, n, k, c):
        if n == 1:
            if c % 2 == 0:
                return '0'
            else:
                return '1'
            return 1
        if k > lo[n]//2+1:
            return self.getK(lo, n-1, lo[n]-k+1, c+1)
        elif k == lo[n]//2+1:
            if c % 2 == 0:
                return '1'
            else:
                return '0'
        else:
            return self.getK(lo, n-1, k, c)


s = Solution()
n = 4
k = 11
print(s.findKthBit(n, k))
