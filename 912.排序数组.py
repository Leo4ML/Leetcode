'''
给你一个整数数组 nums，将该数组升序排列。
示例 1：
输入：nums = [5,2,3,1]
输出：[1,2,3,5]
示例 2：
输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]

提示：
1 <= nums.length <= 50000
-50000 <= nums[i] <= 50000
通过次数30,049提交次数52,878
'''

from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        arr = nums
        if len(arr) <= 1:
            return arr
        l = -1
        r = len(arr)-1
        cur = 0
        while cur < r:
            if arr[cur] < arr[-1]:
                arr[l+1], arr[cur] = arr[cur], arr[l+1]
                l += 1
                cur += 1
            elif arr[cur] == arr[-1]:
                cur += 1
            else:
                arr[cur], arr[r-1] = arr[r-1], arr[cur]
                r -= 1
        arr[r], arr[-1] = arr[-1], arr[r]
        r += 1
        arr[:l+1] = self.sortArray(arr[:l+1])
        arr[r:] = self.sortArray(arr[r:])
        return arr


s = Solution()
nums = [5, 2, 3, 1]
print(s.sortArray(nums))
