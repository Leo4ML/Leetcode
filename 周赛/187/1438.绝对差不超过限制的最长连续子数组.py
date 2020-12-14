'''
给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，
该子数组中的任意两个元素之间的绝对差必须小于或者等于 limit 。
如果不存在满足条件的子数组，则返回 0 。

示例 1：
输入：nums = [8,2,4,7], limit = 4
输出：2 
解释：所有子数组如下：
[8] 最大绝对差 |8-8| = 0 <= 4.
[8,2] 最大绝对差 |8-2| = 6 > 4. 
[8,2,4] 最大绝对差 |8-2| = 6 > 4.
[8,2,4,7] 最大绝对差 |8-2| = 6 > 4.
[2] 最大绝对差 |2-2| = 0 <= 4.
[2,4] 最大绝对差 |2-4| = 2 <= 4.
[2,4,7] 最大绝对差 |2-7| = 5 > 4.
[4] 最大绝对差 |4-4| = 0 <= 4.
[4,7] 最大绝对差 |4-7| = 3 <= 4.
[7] 最大绝对差 |7-7| = 0 <= 4. 
因此，满足题意的最长子数组的长度为 2 。

示例 2：
输入：nums = [10,1,2,4,7,2], limit = 5
输出：4 
解释：满足题意的最长子数组是 [2,4,7,2]，其最大绝对差 |2-7| = 5 <= 5 。

示例 3：
输入：nums = [4,2,2,2,4,4,2,2], limit = 0
输出：3
 
提示：
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
0 <= limit <= 10^9
'''
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        result = 1
        i = j = 0
        while i < len(nums):
            num_min = 10**9
            num_max = 0
            while i <= j < len(nums):
                if num_max <= nums[j]:
                    max_idx = j
                if num_min >= nums[j]:
                    min_idx = j
                num_min = min(num_min, nums[j])
                num_max = max(num_max, nums[j])
                if num_max-num_min > limit:
                    break
                else:
                    result = max(result, j-i+1)
                    j += 1
            i = min(max_idx, min_idx) + 1
            j = i
        return result

s = Solution()
nums = [4,2,2,2,4,4,2,2]
limit = 0
print(s.longestSubarray(nums, limit))