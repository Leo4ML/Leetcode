'''
给你一个正整数数组 nums ，请你从中删除一个含有若干不同元素的子数组。删除子数组的得分
就是子数组各元素之和 。返回只删除一个子数组可获得的最大得分 。
如果数组 b 是数组 a 的一个连续子序列，即如果它等于 a[l],a[l+1],...,a[r] ，那么它就是 a 的一个子数组。

示例 1：
输入：nums = [4,2,4,5,6]
输出：17
解释：最优子数组是 [2,4,5,6]

示例 2：
输入：nums = [5,2,1,2,5,2,1,2,5]
输出：8
解释：最优子数组是 [5,2,1] 或 [1,2,5]

提示：
1 <= nums.length <= 105
1 <= nums[i] <= 104
'''
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        start = end = 0
        tmp = []
        res = 0
        while start < len(nums) and end < len(nums):
            if nums[end] not in tmp:
                tmp.append(nums[end])
                res = max(res, sum(tmp))
                end += 1
            else:
                start = start+nums[start:end].index(nums[end])+1
                end = start
                tmp = []
        return res


s = Solution()
nums = [4,2,4,5,6]
print(s.maximumUniqueSubarray(nums))
