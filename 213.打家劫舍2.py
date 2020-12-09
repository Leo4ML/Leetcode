'''
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，
这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻
的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [2,3,2]
输出: 3
解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
示例 2:

输入: [1,2,3,1]
输出: 4
解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。
'''
# dp[i]表示前i个房间取得最大值（不一定取第i个）
# dp[i]=max(dp[i-2]+nums[i],dp[i-1])
# 如果取了第一个房子，则不能取最后一个房子；

'''
class Solution:
    def rob(self, nums):
        dp1 = [0]*(len(nums))
        dp2 = [0]*(len(nums))
        dp = [0]*(len(nums))
        if len(nums) == 0:
            return 0
        if len(nums) <= 3:
            return max(nums)
        if len(nums)==4:
            return max(nums[0]+nums[2],nums[1]+nums[3])
        # 取第一个数
        dp1[0] = nums[0]
        dp1[1] = max(nums[0],nums[1])
        for i in range(2, len(nums)-1):
            dp1[i] = max(dp1[i-2]+nums[i], dp1[i-1])
        print(dp1)
        # 第一个数不取
        dp2[0] = 0
        dp2[1] = nums[1]
        dp2[2] = max(nums[1], nums[2])
        for i in range(3, len(nums)):
            dp2[i] = max(dp2[i-2]+nums[i], dp2[i-1])
        print(dp2)
        return max(dp2[-1],dp1[-2])
'''
# 简洁写法！巧用cur 和 pre代替dp[i-1]和dp[i-2]!


class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        def getmax(arr):
            cur, pre = 0, 0
            for i in range(len(arr)):
                cur, pre = max(pre+arr[i], cur), cur
            return cur
        return max(getmax(nums[1:]), getmax(nums[:-1]))


s = Solution()
print(s.rob([1, 1, 3, 6, 7, 10, 7, 1, 8, 5, 9, 1, 4, 4, 3]))
