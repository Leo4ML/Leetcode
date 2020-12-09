'''
给你一个整数数组 nums 和一个整数 k。
如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。
请返回这个数组中「优美子数组」的数目。

示例 1：
输入：nums = [1,1,2,1,1], k = 3
输出：2
解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
示例 2：
输入：nums = [2,4,6], k = 1
输出：0
解释：数列中不包含任何奇数，所以不存在优美子数组。
示例 3：
输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
输出：16

提示：
1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
'''

from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        if len(nums) < 3:
            return 0

        def findk():
            res = []
            n = len(nums)
            cur = 0
            ods = 0
            start = -1
            while cur < n:
                if nums[cur] % 2 == 1:
                    ods += 1
                    if start == -1:
                        start = cur
                    if ods == k:
                        res.append((start, cur))
                        if nums[start] % 2 == 1:
                            ods -= 1
                        if start+1<len(nums):
                            while nums[start+1] % 2 != 1:
                                start += 1
                            start += 1

                cur += 1
            return res
        r = findk()
        count = 0
        for start, end in r:
            cs, ce = 0, 0
            while start-1 >= 0 and nums[start-1] % 2 == 0:
                cs += 1
                start -= 1
            while end+1 < len(nums) and nums[end+1] % 2 == 0:
                ce += 1
                end += 1
            count += (cs+1)*(ce+1)
        return count


def findk():
    res = []
    n = len(nums)
    cur = 0
    ods = 0
    start = -1
    while cur < n:
        if nums[cur] % 2 == 1:
            ods += 1
            if start == -1:
                start = cur
            if ods == k:
                res.append((start, cur))
                if nums[start] % 2 == 1:
                    ods -= 1
                if start+1<len(nums):
                    while nums[start+1] % 2 != 1:
                        start += 1
                    start += 1

        cur += 1
    return res


nums = [2044,96397,50143]
k = 1
s = Solution()
print(s.numberOfSubarrays(nums, k))
print(findk())
