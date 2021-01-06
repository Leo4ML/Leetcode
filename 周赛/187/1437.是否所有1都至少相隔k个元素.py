'''
给你一个由若干 0 和 1 组成的数组 nums 以及整数 k。如果所有 1 都至少相隔 k 个元素，则返回 True ；否则，返回 False 。

示例 1：
输入：nums = [1,0,0,0,1,0,0,1], k = 2
输出：true
解释：每个 1 都至少相隔 2 个元素。

示例 2：
输入：nums = [1,0,0,1,0,1], k = 2
输出：false
解释：第二个 1 和第三个 1 之间只隔了 1 个元素。

示例 3：
输入：nums = [1,1,1,1,1], k = 0
输出：true

示例 4：
输入：nums = [0,1,0,1], k = 1
输出：true
 
提示：
1 <= nums.length <= 10^5
0 <= k <= nums.length
nums[i] 的值为 0 或 1
'''
from typing import List
class Solution:
    # 0和1两个指针做数零操作
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        one = 0
        while one < len(nums):
            if nums[one] == 1:
                count = 0
                zero = one + 1
                while zero < len(nums) and nums[zero] == 0:
                    count += 1
                    zero += 1
                if count < k and one < len(nums)-1 and zero < len(nums):
                    return False
                one = zero
            else:
                one += 1
        return True
    # 字符串操作
    def kLengthApart2(self, nums: List[int], k: int) -> bool:
        nums = ''.join(list(map(str, nums))).strip('0')
        new = nums.split('1')[1:-1]
        for num in new:
            if len(num) < k:
                return False
        return True
    # 数零：从第一个1开始，碰到下一个1之前，连续0的个数与k做判断
    def kLengthApart3(self, nums: List[int], k: int) -> bool:
        cur = 0
        flag = 0
        count = 0
        while cur < len(nums):
            if nums[cur] == 1:
                if flag == 0:
                    flag = 1
                else:
                    if count < k:
                        return False
                    count = 0
                cur += 1
            elif nums[cur] == 0 and flag == 0:
                cur += 1
            elif nums[cur] == 0 and flag == 1:
                count += 1
                cur += 1
        # 官方参考题解，记录上一个1的坐标，计算中间多少个0即可
        return True

                

s = Solution()
nums = [1,1,1,1,1]
k = 0
print(s.kLengthApart3(nums, k))