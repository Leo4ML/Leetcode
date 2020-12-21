from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # dp = [[-999999999]*len(nums) for _ in range(k)]
        # for i in range(k):
        #     dp[i][0] = nums[0]
        #     if i > 0:
        #         dp[i][1] = -99999999999
        # #print(dp)
        # for j in range(1, len(nums)):
        #     for i in range(k):
        #         if j-i-1 >= 0:
        #             #print([dp[m][j-i-1] for m in range(k)])
        #             dp[i][j] = max([dp[m][j-i-1] for m in range(k)])+nums[j]
        #             #print(dp[i][j])
        #     dp2[j] = max([dp[m][len(nums)-1] for m in range(k)])
        # res = max([dp[m][len(nums)-1] for m in range(k)])
        # #print(dp)
        return res
    def maxResult2(self, nums: List[int], k: int) -> int:
        dp = [None]*len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if i-k >= 0:
                start = i-k
            else:
                start = 0
            dp[i] = max(dp[start:i])+nums[i]
        return dp[-1]
s = Solution()
nums = [1,-5,-20,4,-1,3,-6,-3]
k = 2
print(s.maxResult2(nums, k))
