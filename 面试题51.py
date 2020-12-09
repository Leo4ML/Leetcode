'''
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
示例 1:

输入: [7,5,6,4]
输出: 5
'''

from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        new_nums = sorted(nums)
        visited = [0 for _ in range(len(new_nums))]
        cnt = 0
        for i in range(len(nums)):
            if nums[i] != new_nums[i]:
                for j in range(len(new_nums)):
                    if new_nums[j] == nums[i] and visited[j] == 0:
                        visited[j] = 1
                        if j > i:
                            tmp = j-i 
                        if j < i and 
                        i-j-1
                        cnt += tmp
        return cnt


s = Solution()
nums = [2, 1, 1]
print(s.reversePairs(nums))
