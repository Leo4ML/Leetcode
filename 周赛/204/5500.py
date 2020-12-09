'''
给你一个整数数组 nums ，请你求出乘积为正数的最长子数组的长度。
一个数组的子数组是由原数组中零个或者更多个连续数字组成的数组。
请你返回乘积为正数的最长子数组长度。

示例  1：
输入：nums = [1,-2,-3,4]
输出：4
解释：数组本身乘积就是正数，值为 24 。

示例 2：
输入：nums = [0,1,-2,-3,-4]
输出：3
解释：最长乘积为正数的子数组为 [1,-2,-3] ，乘积为 6 。
注意，我们不能把 0 也包括到子数组中，因为这样乘积为 0 ，不是正数。

示例 3：
输入：nums = [-1,-2,-3,0,1]
输出：2
解释：乘积为正数的最长子数组是 [-1,-2] 或者 [-2,-3] 。

示例 4：
输入：nums = [-1,2]
输出：1

示例 5：
输入：nums = [1,2,3,5,-6,4,0,10]
输出：4
 
提示：
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
'''
from typing import List


class Solution:
    # def getMaxLen(self, nums: List[int]) -> int:
    #     res = 0
    #     for i in range(len(nums)):
    #         if nums[i] == 0:
    #             continue
    #         c = 0
    #         minis = 0
    #         for j in range(i, len(nums)):
    #             if nums[j] > 0:
    #                 c += 1
    #             elif nums[j] < 0:
    #                 c += 1
    #                 minis += 1
    #             if minis % 2 == 0:
    #                 res = max(res, c)
    #             if nums[j] == 0:
    #                 c = 0
    #                 minis = 0
    #     return res
    def getMaxLen(self, nums: List[int]) -> int:
        dp = [[0]*2 for _ in range(len(nums)+1)]
        res = 0
        for i in range(1, len(nums)+1):
            if nums[i-1] > 0:
                dp[i][1] = dp[i-1][1] + 1
                if dp[i][0] > 0:
                    dp[i][0] = dp[i-1][0] + 1
            if nums[i-1] < 0:
                if dp[i-1][0] > 0:
                    dp[i][1] = dp[i-1][0]+1
                dp[i][0] = dp[i-1][1]+1
            res = max(dp[i][1], res)
        print(dp)
        return res



s = Solution()
nums = [-16,0,-5,2,2,-13,11,8]
print(s.getMaxLen(nums))
