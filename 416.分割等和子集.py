'''
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
注意:
每个数组中的元素不会超过 100
数组的大小不会超过 200
示例 1:
输入: [1, 5, 11, 5]
输出: true
解释: 数组可以分割成 [1, 5, 5] 和 [11].
 
示例 2:
输入: [1, 2, 3, 5]
输出: false
解释: 数组不能分割成两个元素和相等的子集.
'''
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums or sum(nums) %2 == 1:
            return False
        target = sum(nums)//2
        dp = [[0]*target] for i in range(len(nums+1))
        dp[0][0] = 1

    def find()



nums = [1, 2, 3, 4, 5, 6, 7]
s = Solution()
print(s.canPartition(nums))