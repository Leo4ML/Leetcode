'''
给出一个区间的集合，请合并所有重叠的区间。

示例 1:
输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:
输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
'''

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        intervals.sort()
        cur = 1
        while cur < len(intervals):
            if intervals[cur][0] <= intervals[cur-1][1]:
                intervals.insert(cur+1, [intervals[cur-1][0], max(intervals[cur][1], intervals[cur-1][1])])
                del intervals[cur-1]
                del intervals[cur-1]
            else:
                cur += 1
        return intervals


s = Solution()
intervals = [[1, 4], [2, 3]]
print(s.merge(intervals))
